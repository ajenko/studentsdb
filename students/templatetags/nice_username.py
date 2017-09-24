from django import template

register = template.Library()

@register.filter
def nice_username(user):
	""" Return 'full_name' or if it doesn`t exist - 'username' """
	name = user.get_full_name()
	if not name:
		name = user.username
	return name
