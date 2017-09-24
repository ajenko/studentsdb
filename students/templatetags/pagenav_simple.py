from django import template

register = template.Library()
# Usage: {% pagenav_simple objects_list=students is_paginated=is_paginated paginator=paginator %}

@register.simple_tag
def pagenav_simple(*args, **kwargs):
	t = template.loader.get_template('students/pagination.html')
	return t.render({
			'objects_list': kwargs['objects_list'],
			'is_paginated': kwargs['is_paginated'],
			'paginator': kwargs['paginator']
			})