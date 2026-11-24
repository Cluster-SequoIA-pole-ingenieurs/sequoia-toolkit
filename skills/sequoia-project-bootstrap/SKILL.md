---
name: sequoia-project-bootstrap
description: Create or update a project's short AGENTS.md from a validated SequoIA kick-off document and repository evidence. Use after kick-off validation or when agreed scope, tooling, scientific constraints, or AI usage policy changes. Produces a reviewable file, verification report, and unresolved questions.
---

# SequoIA Project Bootstrap

## Purpose and scope

Turn the agreed project framing and the repository's actual development workflow
into concise, durable instructions for an engineer's coding agent. The kick-off
remains the source of project decisions; `AGENTS.md` records only what changes
how the agent should work in this repository. Reusable procedures belong in
skills, with links from `AGENTS.md` when useful.

Create or update the file in the target project repository, which may differ
from the repository containing this skill. Do not create instructions for
`sequoia-toolkit` merely because this skill is installed there.

This task does not authorize changes to code, the kick-off, CI, agent settings,
or skill installations. Do not commit, push, publish, create issues, contact
project members, or change access rights as part of bootstrapping.

## Inputs

Use the following inputs, asking only for missing information needed to proceed:

- The target repository root and destination, normally its root `AGENTS.md`.
- The validated kick-off document, or an approved extract with its validation
  evidence and applicable AI policy. A path, accessible link, or pasted text works.
- Any explicitly approved amendments and relevant institutional restrictions.
- Existing repository guidance and any reusable skills available to this project.

Use the project's established documentation language. If none is established,
use French for SequoIA working documents unless the user requests another language.

## Workflow

### 1. Establish readiness and permitted access

Before inspecting project code or data, establish whether the current assistant,
environment, intended activity, and information to be read are permitted by the
project's AI policy. Do not fetch a restricted kick-off through an external
service to discover whether doing so is allowed. If the permitted scope is
unknown, ask for the policy decision or an approved extract first.

Check the kick-off's validation status and confirmations. For documents following
the SequoIA template, use section 8 for validation, section 3.1 for the start
decision, and section 4 for AI usage. Equivalent evidence in another format is
acceptable. A date, filename, or completed template alone does not prove approval.

- If the kick-off is unvalidated, or AI use is prohibited, deferred, or incompatible
  with this environment, stop before further project inspection or file changes.
  Explain the specific missing decision or restriction without quoting sensitive
  content. Do not approve the document or select another provider yourself.
- Validation with reservations or a limited start is usable only within the
  explicitly permitted activities. Preserve relevant limits; an open dependency
  for a later pilot does not automatically block documentation work now.
- If reservations leave this task's authorization unclear, ask for that decision
  and leave the target file unchanged.

Proceed once these prerequisites are established. Do not ask for the same
authorization again when the supplied evidence already covers the work.

### 2. Inspect the repository and build an evidence map

Read applicable existing agent instructions before changing anything. Inspect
the target file, nested instruction files, and other agent guidance where present
to understand their scope and avoid conflicting duplicates. Respect local edits.

Start with the README, contribution guide, dependency/build manifests, CI,
test configuration, and a focused view of the source tree. Read scientific or
infrastructure documentation only where needed. Avoid scanning datasets, model
weights, credentials, or unrelated private material.

Identify the evidence needed for the proposed instructions:

| Guidance | Preferred evidence |
|---|---|
| Engineering objective, scope, exclusions, acceptance criteria | Validated kick-off and approved amendments |
| AI environment, allowed information and prohibited uses | Validated AI decision and applicable institutional rules |
| Installation, build, lint, type checking and tests | Repository configuration, CI and maintained developer documentation |
| Architectural and compatibility constraints | Existing instructions, code, tests and technical documentation |
| Scientific validation and reproducibility requirements | Approved protocol, benchmark specification or documented project decisions |
| Reusable workflows | Skills actually available to the project and their documented triggers |

Keep a compact working record of source paths or sections for substantive rules.
Separate agreed requirements, repository observations, and suggestions. Do not
turn a convention observed in one file into a project-wide requirement.

If sources conflict, report the conflict and its consequence. Do not silently
choose a new project decision or weaken a restriction. Complete independent,
supported sections where possible; defer the affected section or file when the
conflict would make its instructions unsafe or contradictory.

### 3. Draft or update the short AGENTS.md

Aim for approximately 50–100 lines when the project permits it; this is a guide,
not a quota. Keep consequential instructions even if more space is needed. Link
to detailed documents instead of reproducing them. Include only useful sections:

1. **Purpose and boundaries:** a few lines distinguishing the engineering work
   from the long-term research goal, with consequential exclusions and a link to
   the approved scope and acceptance criteria.
2. **Development and verification:** exact repository-specific commands, their
   working directory and relevant prerequisites. Distinguish ordinary local checks
   from cluster, GPU, private-data or external-service checks.
3. **Non-obvious constraints:** architecture, supported environments, scientific
   invariants and compatibility rules that an agent is likely to miss.
4. **AI and information boundaries:** a minimal operational summary of applicable
   allowed environments, uses and information limits, plus a permitted policy
   reference. Do not imply that this file grants access or enforces isolation.
5. **References and relevant skills:** links to maintained technical documentation
   and available skills, stating briefly when each is useful.

Include scientific or HPC requirements only when supported by the project:
for example, benchmark splits, numerical tolerances, units, random seeds,
environment provenance, scheduler variants or job resource limits. Do not invent
cluster names, queues, CUDA versions, commands, metrics or reproducibility promises.
Do not impose the toolkit's Python stack or Slurm/PBS support on every project.

Keep schedules, participant lists, contact details, task status and meeting
minutes in their existing documents. Include a responsible role only when it
changes an engineering decision. Never copy secrets, private dataset locations,
or sensitive contractual content into the file. Check that links themselves are
appropriate for the repository's intended audience; do not copy a private
kick-off into a public repository to make a reference accessible.

Keep non-blocking unknowns and optional recommendations in the delivery report,
not as fabricated requirements or scaffold placeholders. When a restriction
affects current work, retain its operational boundary in `AGENTS.md` even if its
full supporting document is private.

When updating, make the smallest justified diff. Preserve manual additions and
unrelated sections, including existing guidance that is longer than the target.
Remove or replace a rule only with evidence that it is obsolete or superseded;
explain consequential changes. Scope component-specific rules to existing nested
files where appropriate. Do not introduce extra instruction files or agent-specific
copies unless needed and requested. Re-running with unchanged inputs should
produce no substantive changes, including no gratuitous date or layout updates.

### 4. Verify the proposed instructions

Check referenced local paths, command definitions, working directories, and
consistency with applicable instructions. For each command, distinguish:

- **Executed:** run in this task; record the result and relevant environment.
- **Source-checked:** confirmed in repository configuration or documentation,
  but not run here.
- **Requires another environment:** needs unavailable compute, data, credentials
  or services; identify the prerequisite and the check still needed.

Run lightweight local checks when authorized and useful. Inspect what a command
does before executing it. Do not install dependencies, submit scheduler jobs,
start training, consume paid resources, or modify external systems just to
validate documentation without authorization for those actions. Rendering a job
script is not evidence that submission or execution succeeds.

Keep verification status in the delivery report unless an execution prerequisite
is durable guidance for future agents. Do not label a command as tested merely
because it appears in CI, and do not claim scientific correctness from passing
software tests alone.

### 5. Save and present for engineer review

If asked to create or update the file, save the supported changes in the target
repository and present the diff or a concise change summary for engineer review.
Review is not a reason to ask permission before writing the already requested,
reversible local change. If asked only for a draft, return the draft without
modifying the repository. Do not label the result approved on the engineer's behalf.

Deliver:

- The file path and whether it was created, updated, or left unchanged.
- The kick-off version/date and approval evidence used, without unnecessary
  personal or confidential information.
- A short explanation of substantive rules and their sources, highlighting
  conflicts and any existing instruction removed or superseded.
- Verification results, clearly separating executed and source-checked commands
  from checks requiring another environment.
- Remaining questions or blocked sections, with the responsible role only when
  established; do not invent owners or deadlines.

If blocked at readiness, deliver only the specific blocker and the minimum
information needed to continue. If nothing needs updating, say so rather than
rewriting the file. Suggest revisiting the instructions when approved scope,
AI policy, tooling, or recurring engineering feedback changes.
