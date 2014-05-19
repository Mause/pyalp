from django.contrib import admin
from django import forms

from pyalp.utils import render_to_response
from .models import Pizza, PizzaOrder

from pyalp_translation.customization import custom_gettext
_ = custom_gettext('admin_pizza_list')

# Register your models here.
admin.site.register(Pizza)


class ActionForm(forms.Form):
    action = forms.CharField()
    orderid = forms.CharField()


class PizzaOrderAdmin(admin.ModelAdmin):
    def get_urls(self, *args, **kwargs):
        from django.conf.urls import url

        urlpatterns = super().get_urls(*args, **kwargs)
        urlpatterns.insert(
            0,
            url(
                r'^order_summary/$',
                self.admin_site.admin_view(self.order_summary),
                name='pizza_pizzaorder_order_summary'
            )
        )

        return urlpatterns

    def order_summary(self, request):
        if not self.has_change_permission(request):
            return

        form = ActionForm(request.POST)
        if form.is_valid():
            cleaned_data = form.clean()

            # grab the order we want to update
            order = PizzaOrder.objects.filter(id=cleaned_data['orderid'])
            if cleaned_data['action'] == 'pay':
                order.update(paid=True)

            elif cleaned_data['action'] == 'deliver':
                order.update(delivered=True)

            else:
                raise Exception()

        orders = PizzaOrder.objects.all()

        context = {}
        context.update({
            'page_context': 'admin_pizza_list',
            'orders': orders,
            'title': _('singular') + ' ' + _('detail'),
            'opts': self.model._meta
        })

        # context['opts']['app_config'] = {'verbose_name': 'Pizza'}
        context['original'] = 'Pizza'

        return render_to_response(
            'admin/admin_pizza_list.html',
            context,
            context_instance=request
        )

admin.site.register(PizzaOrder, PizzaOrderAdmin)
