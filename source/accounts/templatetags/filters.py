from django.template import Library

register = Library()


@register.filter(name='times')
def times(number):
    return range(number)

# @register.filter(name='average')
# def times(queryset, field, value):
#     rating_number = queryset.objects.filter(field=value).count()
#
#     return range()