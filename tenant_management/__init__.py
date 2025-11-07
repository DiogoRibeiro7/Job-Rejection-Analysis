"""Tenant management module for multi-tenant data isolation.

Provides simple in-memory classes to register and retrieve tenants.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, Optional


@dataclass
class Tenant:
    """Represents a single tenant using the platform."""

    tenant_id: str
    name: str
    metadata: Dict[str, str] = field(default_factory=dict)


class TenantManager:
    """Manage tenants in memory.

    This lightweight manager supports adding, retrieving and listing tenants.
    In a real deployment the manager would interface with a persistent data store
    and handle billing and resource isolation. Here we keep things simple to
    exercise the design in unit tests.
    """

    def __init__(self) -> None:
        self._tenants: Dict[str, Tenant] = {}

    def add_tenant(self, tenant: Tenant) -> None:
        """Register a new tenant.

        Args:
            tenant: The tenant object to store.

        Raises:
            ValueError: If a tenant with the same ``tenant_id`` already exists.
        """

        if tenant.tenant_id in self._tenants:
            raise ValueError(f"Tenant '{tenant.tenant_id}' already exists")
        self._tenants[tenant.tenant_id] = tenant

    def get_tenant(self, tenant_id: str) -> Optional[Tenant]:
        """Retrieve a tenant by identifier."""

        return self._tenants.get(tenant_id)

    def list_tenants(self) -> Iterable[Tenant]:
        """Return all registered tenants."""

        return self._tenants.values()

    def remove_tenant(self, tenant_id: str) -> None:
        """Remove a tenant from the manager.

        Missing tenant IDs are ignored to keep the API forgiving.
        """

        self._tenants.pop(tenant_id, None)
