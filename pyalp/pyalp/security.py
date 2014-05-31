from operator import attrgetter
from pyalp_page.universal import SecurityEnum


def current_security_level(user):
    in_groups = user.groups.all()
    in_groups = map(attrgetter('name'), in_groups)
    in_groups = map(str.upper, in_groups)

    in_groups = {
        getattr(SecurityEnum, level)
        for level in in_groups
        if hasattr(SecurityEnum, level)
    }

    return (
        max(in_groups) if in_groups
        else 0
    )
