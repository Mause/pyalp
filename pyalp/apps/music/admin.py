from django.contrib import admin

# Register your models here.

from apps.music.models import Song, Vote

admin.site.register([Song, Vote])
