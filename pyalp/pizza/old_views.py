# from collections import defaultdict

from django.shortcuts import redirect
from django.contrib.auth.decorators import (
    permission_required,
    user_passes_test,
    login_required,
    REDIRECT_FIELD_NAME
)
from django.core.context_processors import csrf
from django.forms import ModelChoiceField, IntegerField
from django.template import RequestContext
# from django.utils.translation import ugettext as _

from pyalp.utils import render_to_response
from pizza import gettext as _


# import djmoney.forms
from vanilla import CreateView
from floppyforms import forms

from pizza.models import Pizza, PizzaOrder
from flags.registry import flag_registry


def deny_if_flag_disabled(flag_name):
    def internal(function):
        def actual(form, request, *args, **kwargs):
            if flag_registry.is_flag_enabled(flag_name):
                return function(form, request, *args, **kwargs)
            else:
                redirect('index')
        return actual
    return internal


def login_required_with_form(
        function=None, redirect_field_name=REDIRECT_FIELD_NAME,
        login_url=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """

    def internal(form, request, *args, **kwargs):
        def wrapper(*q, **w):
            import pudb
            pu.db
            return function(form, request, *args, **kwargs)

        actual_decorator = user_passes_test(
            lambda u: u.is_authenticated(),
            login_url=login_url,
            redirect_field_name=redirect_field_name
        )
        return actual_decorator(wrapper)(request)

    return internal


@login_required
def index(request):
    orders = PizzaOrder.objects.filter(orderer=request.user)
    return render_to_response(
        'ordered_pizzas.html',
        {'orders': orders}
    )


class OrderForm(forms.Form):
    pizza = ModelChoiceField(
        Pizza.objects.filter(enabled=True)
    )
    pizza.label = (
        _('desc_pizzaid') +
        " (<a href=\"pizza_list.php\">" +
        _('link_pizza_list') +
        "</a>)"
    )

    quantity = IntegerField()
    quantity.label = _("desc_quantity")


class OrderPizzaView(CreateView):
    # @deny_if_flag_disabled('pizza_orders')
    # @login_required
    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            order = PizzaOrder(
                pizza=form.cleaned_data['pizza'],
                orderer=request.user,
                quantity=form.cleaned_data['quantity']
            )
            order.save()

            import pudb
            pu.db
            return redirect('index')
        else:
            return render_to_response('order_pizzas.html')

    # @deny_if_flag_disabled('pizza_orders')
    # @login_required
    def get(self, request):
        args = csrf(request)
        args['order_form'] = OrderForm()
        args['pizza_orders_locked'] = flag_registry.is_flag_enabled(
            'pizza_orders_locked')
        return render_to_response(
            'order_pizzas.html', args,
            context_instance=RequestContext(request)
        )

    # @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderPizzaView, self).dispatch(*args, **kwargs)

# @deny_if_flag_disabled('pizza_orders')
# @login_required
# def order_pizza(request):
#     import pudb
#     pu.db
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         print(form)
#         if form.is_valid():
#             order = PizzaOrder(
#                 pizza=form.cleaned_data['pizza'],
#                 orderer=request.user,
#                 quantity=form.cleaned_data['quantity']
#             )
#             order.save()

#             return redirect('index')
#         else:
#             return render_to_response('order_pizzas.html')
#     else:
#         args = {'order_form': OrderForm()}
#         args.update(csrf(request))
#         return render_to_response('order_pizzas.html', args)


def pizza_details(request):
    args = {
        'pizza_options': Pizza.objects.filter(enabled=True)
    }

    return render_to_response('pizza_list.html', args)


@login_required
@permission_required('pizza.can_access_orders')
def admin_pizza_order_list(request):
    orders = PizzaOrder.objects.filter(
        paid=True,
        delivered=False
    )

    summary = {}
    pizzas = {}
    totals = {}
    # import pudb
    # pu.db

    # for order in orders:
    #     summary[order['id']]['delivered'] += (order['delivered'] * order['quantity'])
    #     totals['delivered'] += (order['delivered'] * order['quantity'])
    #     if (order['delivered'] > 0):
    #         summary[order['id']]['quantity'] += 0
    #         totals['quantity'] += 0
    #     else:
    #         summary[order['id']]['quantity'] += order['quantity']
    #         totals['quantity'] += order['quantity']

    #     if order['paid']:
    #         summary[order['id']]['paid'] += (order['paid'] * order['quantity'])
    #         totals['paid'] += (order['paid'] * order['quantity'])
    #         summary[order['id']]['price'] += 0
    #         totals['price'] += 0
    #     else:
    #         summary[order['id']]['paid'] += 0
    #         totals['paid'] += 0
    #         summary[order['id']]['price'] += (order['price']*order['quantity'])
    #         totals['price'] += (order['price']*order['quantity'])

    #     if order['id'] not in pizzas:
    #         pizzas[order['id']] = order['pizza']

    args = {
        'pizza_orders': orders
    }
    return render_to_response('admin_pizza_order_list.html', args)
