"""Create a new (empty) Access database."""

from __future__ import annotations

__all__: Final[tuple[str]] = ("create",)

from typing import Final

from msaccessdb._create import create

__version__: Final[str] = "1.0.0"
