from pyalp.utils import render_to_response


def index(request):
    context = {
        'page_context': 'global'
    }

    return render_to_response(
        'home.html',
        context,
        context_instance=request
    )
