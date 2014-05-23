from os.path import join

from django import template
from django.template.loader import render_to_string

from pyalp_translation.customization import custom_gettext
_ = custom_gettext('')

from common.generic_template_tag import (
    split_into_variables,
    GenericTemplateTag
)
register = template.Library()


class Display(GenericTemplateTag):
    def __init__(self, nodelist, modjool=True, side=True):
        self.nodelist = nodelist

        self.modjool = modjool
        self.side = side

    def render(self, context):
        skin = context['skin']

        if 'image_text' in skin.colors:
            color = skin.colors['image_text']
        else:
            color = 'white'

        side = self.resolve(context, self.side)
        if side:
            top = 'include/_top.html'
            bot = 'include/_bot.html'
        else:
            top = 'include/_top_noside.html'
            bot = 'include/_bot_noside.html'

        # if self._security == 3:
        #     title = _("sadministrator") + ': ' + self._name
        # elif self._security == 2:
        #     title = _("administrator") + ': ' + self._name
        # else:
        #     title = self._name

        render_context = {
            'copyright_img_src': 'img/{}_copyright.gif'.format(color),
            'license_img_src': 'img/{}_license.gif'.format(color),

            'top': top,
            'bottom': bot,

            'skin_top': join(skin.asset_path, '_top.html'),
            'skin_bottom': join(skin.asset_path, '_bot.html'),

            'modjool': self.resolve(context, self.modjool),

            'nodelist_rendered': self.nodelist.render(context)
        }

        print('modjool:', self.modjool)

        return render_to_string(
            'display.html',
            render_context,
            context_instance=context
        )


@register.tag
def display_top(parser, token):
    nodelist = parser.parse(('display_bottom',))
    parser.delete_first_token()

    variables = split_into_variables(token)
    variables = list(variables)

    return Display(nodelist, *variables)
