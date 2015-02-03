from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
import re

register = template.Library()

def mult(value, arg):
    "Multiplies the arg and the value"
    return int(value) * int(arg)
mult.is_safe = False

def sub(value, arg):
    "Subtracts the arg from the value"
    return int(value) - int(arg)
sub.is_safe = False

def div(value, arg):
    "Divides the value by the arg"
    return int(value) / int(arg)
div.is_safe = False

# The purpose of this filter (found online) is to strip JS tags and keep HTML
# I don't know if it's enough to sanitize the inputs though
# Hence, the comment section won't get labeled as safe since it's a public part
@stringfilter
def stripjs(value):
    stripped = re.sub(r'<script(?:\s[^>]*)?(>(?:.(?!/script>))*</script>|/>)', '', force_unicode(value), flags=re.S)
    return mark_safe(stripped)

register.filter('mult', mult)
register.filter('sub', sub)
register.filter('div', div)
register.filter('stripjs',stripjs)
