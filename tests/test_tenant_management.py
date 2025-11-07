import pytest

from tenant_management import Tenant, TenantManager


def test_add_and_get_tenant() -> None:
    manager = TenantManager()
    tenant = Tenant(tenant_id="t1", name="Acme Corp")
    manager.add_tenant(tenant)
    assert manager.get_tenant("t1") == tenant


def test_duplicate_tenant_raises() -> None:
    manager = TenantManager()
    tenant = Tenant(tenant_id="t1", name="Acme Corp")
    manager.add_tenant(tenant)
    with pytest.raises(ValueError):
        manager.add_tenant(tenant)


def test_remove_tenant() -> None:
    manager = TenantManager()
    tenant = Tenant(tenant_id="t1", name="Acme Corp")
    manager.add_tenant(tenant)
    manager.remove_tenant("t1")
    assert manager.get_tenant("t1") is None
