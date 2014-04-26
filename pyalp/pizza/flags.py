from flags.registry import flag_registry


def register_flags():
    flag_registry.add_flag('pizza_orders_locked', False)
