from django import template
register = template.Library()

# Usage: {% pagenav_inclusion object_list=student is_paginated=is_paginated paginator=paginator %}


@register.inclusion_tag('students/pagination.html')
def pagenav_inclusion(object_list, is_paginated, paginator):
    """ Display the navigation page for given list of objects """
    return {
        'object_list': object_list,
        'is_paginated': is_paginated,
        'paginator': paginator
    }
