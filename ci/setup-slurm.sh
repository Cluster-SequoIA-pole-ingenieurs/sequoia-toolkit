#!/usr/bin/env bash
# Installe et demarre un Slurm mono-noeud pour les tests d'integration.
# Utilise par la CI (Ubuntu 24.04) ; a lancer avec sudo. Sans comptabilite :
# le toolkit se rabat alors sur scontrol, ce qui teste aussi ce chemin.
set -euo pipefail

DEBIAN_FRONTEND=noninteractive apt-get update -qq
DEBIAN_FRONTEND=noninteractive apt-get install -y -qq slurm-wlm munge >/dev/null

HOST=$(hostname -s)
CPUS=$(nproc)
mkdir -p /etc/slurm /var/spool/slurmctld /var/spool/slurmd /var/log/slurm /run/munge
[ -f /etc/munge/munge.key ] || dd if=/dev/urandom bs=1 count=1024 of=/etc/munge/munge.key 2>/dev/null
chown munge:munge /etc/munge/munge.key /run/munge
chmod 400 /etc/munge/munge.key
pgrep munged >/dev/null || runuser -u munge -- /usr/sbin/munged

cat > /etc/slurm/slurm.conf << CONF
ClusterName=ci
SlurmctldHost=${HOST}
SlurmUser=root
AuthType=auth/munge
ProctrackType=proctrack/linuxproc
TaskPlugin=task/none
SchedulerType=sched/backfill
SelectType=select/cons_tres
ReturnToService=2
StateSaveLocation=/var/spool/slurmctld
SlurmdSpoolDir=/var/spool/slurmd
SlurmctldLogFile=/var/log/slurm/slurmctld.log
SlurmdLogFile=/var/log/slurm/slurmd.log
JobAcctGatherType=jobacct_gather/none
AccountingStorageType=accounting_storage/none
NodeName=${HOST} CPUs=${CPUS} State=UNKNOWN
PartitionName=debug Nodes=${HOST} Default=YES MaxTime=INFINITE State=UP
CONF

slurmctld -c
sleep 2
slurmd -c
for _ in $(seq 1 30); do
  sinfo -h -o "%T" | grep -q idle && { sinfo; exit 0; }
  sleep 1
done
echo "Slurm n'a pas demarre" >&2
tail -n 50 /var/log/slurm/*.log >&2
exit 1
