from django.db import models
from django.contrib.auth.models import User

import djmoney.models


class Pizza(models.Model):
    """
    Represents a type of Pizza people can order
    """

    """
    "pizza" => "
        `pizzaid` bigint(20) NOT NULL auto_increment,
        `pizza` varchar(150) NOT NULL default '',
        `description` varchar(255) NOT NULL default '',
        `price` decimal(20, 2) NOT NULL default '0',
        `enabled` tinyint(1) NOT NULL default '0',
        UNIQUE KEY `id` (`pizzaid`),
        KEY `pizza` (`pizza`)"
    """

    pizza = models.CharField(
        max_length=150,
        help_text="Pizza name"
    )

    # `description` varchar(255) NOT NULL default '',
    description = models.TextField(
        "A description of toppings, nutritional information, etc"
    )

    # `price` decimal(20, 2) NOT NULL default '0',
    price = djmoney.models.fields.MoneyField(
        "The price and currency for the pizza",
        decimal_places=2, max_digits=20, default_currency='AUD'
    )

    # `enabled` tinyint(1) NOT NULL default '0',
    enabled = models.BooleanField(
        "Toggle the availability of this type of Pizza"
    )

    def __str__(self):
        return '{} for {}'.format(self.pizza, self.price)


class PizzaOrder(models.Model):
    """
    Resolves the many-to-many relationship between users and pizza's
    """
    # `userid` bigint(20) NOT NULL default '0',
    orderer = models.ForeignKey(
        User,
        help_text="The user that made this order"
    )

    # `pizzaid` varchar(150) NOT NULL default '0',
    pizza = models.ForeignKey(
        Pizza,
        help_text="The pizza that was ordered"
    )

    # `quantity` bigint(20) NOT NULL default '0',
    quantity = models.BigIntegerField(
        help_text="Number of the type of pizza that was ordered"
    )

    # `paid` tinyint(1) NOT NULL default '0',
    paid = models.BooleanField(
        default=False,
        help_text="Whether the order has been paid for"
    )

    # `delivered` tinyint(1) NOT NULL default '0',
    delivered = models.BooleanField(
        default=False,
        help_text="Whether the order has been delivered"
    )

    def __str__(self):
        return '{}, {} PizzaOrder of {} {} by {}'.format(
            'paid' if self.paid else 'unpaid',
            'delivered' if self.delivered else 'undelivered',
            self.quantity,
            self.pizza.pizza,
            self.orderer
        )
