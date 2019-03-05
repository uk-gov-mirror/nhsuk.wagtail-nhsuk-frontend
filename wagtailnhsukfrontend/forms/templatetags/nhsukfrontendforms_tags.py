from django import template

register = template.Library()

@register.filter
def add_class(widget, new_class):

    attrs = widget['attrs']

    if hasattr(attrs, 'class'):
        attrs['class'] = attrs['class'] + " " + new_class
    else:
        attrs['class'] = new_class

    widget['attrs'] = attrs
    return widget
