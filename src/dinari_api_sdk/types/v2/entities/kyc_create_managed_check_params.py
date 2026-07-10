# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .jurisdiction import Jurisdiction

__all__ = ["KYCCreateManagedCheckParams"]


class KYCCreateManagedCheckParams(TypedDict, total=False):
    jurisdiction: Jurisdiction
    """Jurisdiction for the KYC check. Defaults to BASELINE."""
