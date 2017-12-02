from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dict, key):
  try:
    return dict[key]
  except:
    return None
