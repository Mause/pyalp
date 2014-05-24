from os.path import join

from django.http import HttpResponse
from django.template.context import Context
from django.template.loader import select_template
from django.views.decorators.cache import cache_page

from pyalp.skin import get_skin

MINUTE = 60


@cache_page(MINUTE * 15)
def skin_css(request):
    skin = get_skin()

    dirs = [
        join(skin.asset_path, 'x.css'),
        join(skin.asset_path, 'css', 'x.css')
    ]
    template = select_template(dirs)

    context = Context({
        'skin': get_skin()
    })

    return HttpResponse(
        template.render(context),
        content_type='text/css'
    )
