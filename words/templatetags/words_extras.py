from django import template
from words.models import Entry

register = template.Library()


class EntryArchive(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        dates = Entry.objects.filter(published=True).datetimes('published_on', 'month', order='DESC')
        if dates:
            print(dates, self.var_name)
            context[self.var_name] = dates
        return ''


@register.tag
def get_entry_archive(parser, token):
    try:
        print(token)
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    var_name = token.contents.split()[2]
    return EntryArchive(var_name)
