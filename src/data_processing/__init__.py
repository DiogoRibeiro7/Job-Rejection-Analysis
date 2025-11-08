"""Data processing module for job rejection analysis.

This module includes:
- email_scraper: Utilities for collecting public job rejection templates
- validation: Schema validation utilities
- schema_versioning: Versioned schema management
- tenant_management: Multi-tenant data isolation
"""

from . import email_scraper
from . import validation
from . import schema_versioning
from . import tenant_management

__all__ = [
    "email_scraper",
    "validation",
    "schema_versioning",
    "tenant_management",
]
