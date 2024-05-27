"""Create a new (empty) Access database."""

from __future__ import annotations

__all__: list[str] = ["create"]
__version__: Final[str] = "1.0.0"

from typing import Final

from msaccessdb._create import create
