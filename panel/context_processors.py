from .registry import MODEL_REGISTRY


def panel_registry(request):
    """Makes `registry` available in every template that extends base_panel.html,
    so the sidebar always lists all models without each view passing it manually."""
    return {'registry': MODEL_REGISTRY}