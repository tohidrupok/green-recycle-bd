from django import template

register = template.Library()


@register.filter
def get_attr(obj, field_name):
    """Usage: {{ item|get_attr:field_name }}
    Django's dot lookup can't take a variable as the key, so this filter
    lets item_list.html render list_fields dynamically."""
    value = getattr(obj, field_name, '')
    if callable(value):
        value = value()
    return value