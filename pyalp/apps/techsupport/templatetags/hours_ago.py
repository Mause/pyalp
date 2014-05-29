from common.generic_template_tag import GenericTemplateTag
from django.utils import timezone


class HoursAgoNode(GenericTemplateTag):
    def __init__(self, time):
        self.time = time

    def render(self, context):
        time = self.resolve(context, self.time)

        time = timezone.now() - time
        time = round(time.total_seconds() / 3600)
        if time != 0:
            return '{:.0f} hour{} ago'.format(time, 's' if time != 1 else '')
        else:
            return 'now'


from django.template import Library
register = Library()
register.tag('hours_ago', HoursAgoNode.invoke)
