import types

from src.web import dashboard


class DummyStreamlit(types.SimpleNamespace):
    def __init__(self):
        super().__init__(
            title=lambda *args, **kwargs: None,
            subheader=lambda *args, **kwargs: None,
            write=lambda *args, **kwargs: None,
            bar_chart=lambda *args, **kwargs: None,
        )


def test_main_runs(monkeypatch):
    dummy = DummyStreamlit()
    monkeypatch.setattr(dashboard, "st", dummy)
    dashboard.main()
