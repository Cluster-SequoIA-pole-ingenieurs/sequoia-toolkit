"""Petits decorateurs utilitaires partages (retry, chronometrage).

Volontairement minimal : pour des besoins de retry avances (backoff
exponentiel, jitter, etc.), preferer une dependance dediee (ex: `tenacity`)
en extra optionnel dans la librairie appelante plutot que d'alourdir
sequoia-core.
"""

from __future__ import annotations

import functools
import time
from collections.abc import Callable
from typing import TypeVar

from sequoia_toolkit.core.log import get_logger

_log = get_logger(__name__)

T = TypeVar("T")


def timeit(func: Callable[..., T]) -> Callable[..., T]:
    """Journalise la duree d'execution d'une fonction (niveau DEBUG)."""

    @functools.wraps(func)
    def wrapper(*args: object, **kwargs: object) -> T:
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            _log.debug("%s termine en %.3fs", func.__qualname__, elapsed)

    return wrapper


def retry(
    times: int = 3,
    delay_seconds: float = 1.0,
    exceptions: tuple[type[BaseException], ...] = (Exception,),
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Reessaie l'appel jusqu'a `times` fois en cas d'exception listee.

    Utile par exemple pour des appels reseau ponctuels (registre de
    modeles, stockage objet) depuis un noeud de calcul.
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args: object, **kwargs: object) -> T:
            last_exc: BaseException | None = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    last_exc = exc
                    _log.warning(
                        "%s a echoue (tentative %d/%d) : %s",
                        func.__qualname__,
                        attempt,
                        times,
                        exc,
                    )
                    if attempt < times:
                        time.sleep(delay_seconds)
            assert last_exc is not None
            raise last_exc

        return wrapper

    return decorator
