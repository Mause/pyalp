from django import template
from django.template.loader import render_to_string

register = template.Library()

from music.models import Song


class ModMusicNode(template.Node):
    def render(self, context):
        if Song.objects.filter(nowplaying=True).count() == 0:
            # random play mode
            random = True
            nowplaying = Song.objects.all()[0]
            # SELECT artist, title, plays, votes
            # FROM music
            # WHERE `nowplaying` = '1'
        else:
            # queued play mode
            random = False
            nowplaying = Song.objects.all().order_by('votes')[0]

        cur_context = {
            'user': nowplaying.playing,
            'votes': nowplaying.votes,
            'plays': nowplaying.plays,
            'artist': nowplaying.artist,
            'title': nowplaying.title
        }

        if random:
            # fill random play details to array
            context.update({
                'user': {
                    'username': 'random play'
                }
            })

        context['comingup'] = (
            Song.objects
            .filter(nowplaying=False)
            .order_by('-votes')
            [:5]
        )

        return render_to_string(
            'music.html',
            cur_context,
            context_instance=context
        )


@register.tag
def mod_music(parser, token):
    return ModMusicNode()
