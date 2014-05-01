from pyalp.utils import render_to_response

from django import forms
from django.utils.safestring import mark_safe
from django.shortcuts import redirect

from listjs.widgets import ListJSWidget
from chosen.fields import ChosenModelChoiceField

from pizza import gettext as _
from pizza.models import PizzaOrder, Pizza
from flags.registry import get_flag_registry


def admin_pizza_list(request):
    orders = PizzaOrder.objects.all()

    summary = {}
    pizzas = {}
    totals = {
        'delivered': 0,
        'quantity': 0,
        'paid': 0,
        'price': moneyed.Money(currency='AUD')
    }

    for record in orders:
        summary[record.pizza.id] = {
            'delivered': 0,
            'quantity': 0,
            'paid': 0,
            'price': moneyed.Money(currency='AUD')
        }

        summary[record.pizza.id]['delivered'] += (
            record.delivered * record.quantity
        )

        totals['delivered'] += (record.delivered * record.quantity)
        if record.delivered:
            summary[record.pizza.id]['quantity'] += 1
            totals['quantity'] += 1
        else:
            summary[record.pizza.id]['quantity'] += record.quantity
            totals['quantity'] += record.quantity

        if record.paid:
            summary[record.pizza.id]['paid'] += (
                record.paid * record.quantity
            )
            totals['paid'] += (record.paid * record.quantity)
        else:
            cost = (
                record.pizza.price * record.quantity
            )

            summary[record.pizza.id]['price'] += cost
            totals['price'] += cost

        if record.pizza.id not in pizzas:
            pizzas[record.pizza.id] = record.pizza

    values = []
    for key in pizzas.keys():
        values.append({
            'name': pizzas[key],
            'quantity': summary[key]['quantity'],
            'delivered': summary[key]['delivered'],
            'paid': summary[key]['paid'],
            'price': summary[key]['price']
        })

    summary = ListJSWidget(
        values=values,
        valueNames=['name', 'quantity', 'delivered', 'paid', 'price'],
        show_totals=True
    )

    context = {
        'page_context': 'admin_pizza_list',
        'summary': summary,
        'pizzas': pizzas,
        'totals': totals,
        'orders': orders,
        'pizzaorderssummary': summary.render()
    }

    return render_to_response(
        'admin_pizza_list.html',
        context,
        context_instance=request
    )


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
    valueNames = ['pizza', 'description', 'price']
    pizzas = Pizza.objects.filter(enabled=True)

    values = []
    for pizza in pizzas:
        values.append({})
        for attr in valueNames:
            values[-1][attr] = getattr(pizza, attr)

    details = ListJSWidget(
        values=values,
        valueNames=valueNames,
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
