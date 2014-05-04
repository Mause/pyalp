from os.path import join

from django.template.context import Context
from django.template.loader import select_template
from django.http import HttpResponse

from pyalp.skin import get_skin


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
