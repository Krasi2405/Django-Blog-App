from django import template

register = template.Library()

@register.filter
def isinst(obj, object_type):
	isinstbool = object_type in str(type(obj))
	return isinstbool