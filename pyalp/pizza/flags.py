from flags.registry import get_flag_registry


def register_flags():
    get_flag_registry().add_flag('pizza_orders_locked', False)
