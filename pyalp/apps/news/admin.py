from django.contrib import admin
from django.forms import ModelForm
from django.contrib.admin import widgets
from django import forms

# Register your models here.
from news.models import NewsItem
from news import gettext as _


class NewsItemForm(ModelForm):
    headline = forms.CharField(
        label=_('desc_headline'),
        error_messages={
            'required': _('error_headline')
        }
    )

    itemtime = forms.DateTimeField(
        label=_('desc_itemtime'),
        widget=widgets.AdminSplitDateTime
    )

    news_article = forms.CharField(
        label=_('desc_news_article'),
        widget=forms.Textarea,
        error_messages={
            'required': _('error_news_article')
        }
    )

    hide_item = forms.BooleanField(
        label=_('desc_hide_item'),
        required=False
    )


class NewsItemAdmin(admin.ModelAdmin):
    form = NewsItemForm

    def save_model(self, request, obj, *args):
        obj.author = request.user
        return super().save_model(request, obj, *args)

admin.site.register(NewsItem, NewsItemAdmin)
