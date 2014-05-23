from pyalp.utils import render_to_response

from django import forms
from django.utils.safestring import mark_safe
from django.shortcuts import redirect

from listjs.widgets import ListJSWidget
from chosen.fields import ChosenModelChoiceField

from . import gettext as _
from .models import PizzaOrder, Pizza

from flags.registry import get_flag_registry


class PizzaOrderForm(forms.Form):
    """
    https://www.youtube.com/watch?v=uPD6okhfGzs
    """

    def __init__(self, *args, **kwargs):
        models = kwargs.pop('models')
        super().__init__(*args, **kwargs)

        pizza = ChosenModelChoiceField(
            models,
            required=True,
            error_messages={
                'required': _('error_pizzaid')
            }
        )

        pizza.label = '{} (<a href="/pizza_list.php">{}</a>)'.format(
            _('desc_pizzaid'),
            _('link_pizza_list')
        )
        pizza.label = mark_safe(pizza.label)

        self.fields['pizza'] = pizza
        self.fields.keyOrder = ['pizza', 'quantity']

    quantity = forms.IntegerField(
        min_value=1,
        initial=1,

        required=True,
        label=_('desc_quantity'),
        error_messages={
            'required': _('error_quantity')
        }
    )


def pizza(request):
    if get_flag_registry().get_statusdict()['pizzas_locked']:
        return redirect('/pizza/locked')

    enabled_pizzas = Pizza.objects.filter(enabled=True)

    order_form = PizzaOrderForm(
        request.POST or None,
        models=enabled_pizzas
    )

    context = {
        'page_context': 'pizza',
        'pizzas': enabled_pizzas,
        'order_form': order_form
    }

    if order_form.is_valid():
        clean = order_form.clean()
        po = PizzaOrder(
            pizza=clean['pizza'],
            quantity=clean['quantity'],
            orderer=request.user
        )
        po.save()
        context['model'] = po

        order_form.data = {}
        assert not context['order_form'].data

    return render_to_response(
        'pizza.html',
        context,
        context_instance=request
    )


def pizza_list(request):
    values = Pizza.objects.filter(enabled=True).values()

    details = ListJSWidget(
        values=values,
        valueNames=['pizza', 'description', 'price'],
        show_totals=False
    )

    context = {
        'page_context': 'pizza_list',
        'details': details
    }

    return render_to_response(
        'pizza_list.html',
        context,
        context_instance=request
    )
