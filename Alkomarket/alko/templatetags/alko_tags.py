from django import template

register = template.Library()

@register.inclusion_tag('alko/list_categories.html')
def show_categories(cat_selected=0):
    return {"cats": [], "cat_selected": cat_selected}