from pyalp.utils import render_to_response
# from django.contrib.auth.decorators import permission_required
#     user_passes_test,
#     login_required,
#     REDIRECT_FIELD_NAME
# )
# from django.core.context_processors import csrf
# from django.forms import ModelChoiceField
# from chosen import forms as chosenforms
# , IntegerField
# from pizza import gettext as _

import moneyed
from listjs.widgets import ListJSWidget

from pizza.models import PizzaOrder, Pizza


def index(request):
    return render_to_response(
        'index.html',
        context_instance=request
    )


def admin_pizza(request):
    return render_to_response(
        'admin_pizza.html',
        context_instance=request
    )


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


def chng_pizza(request):
    return render_to_response(
        'chng_pizza.html',
        context_instance=request
    )


def pizza(request):
    return render_to_response(
        'pizza.html',
        {'page_context': 'pizza'},
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
