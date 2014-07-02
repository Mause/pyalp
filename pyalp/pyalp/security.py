from operator import attrgetter

from django import forms

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


class PrivSelect(forms.Select):
    def __init__(self, *args, **kwargs):
        from pyalp_translation.customization import custom_gettext
        _ = custom_gettext('admin_schedule')

        choices = (
            (0, _('guest')),
            (1, _('user')),
            (2, _('administrator')),
            (3, _('sadministrator'))
        )
        super().__init__(choices=choices, *args, **kwargs)
