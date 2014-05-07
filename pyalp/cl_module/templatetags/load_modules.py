from cl_module.cl_module import ModuleManager

from common.generic_template_tag import GenericTemplateTag


class LoadModulesNode(GenericTemplateTag):
    def __init__(self, breaker=None, into_var='modules'):
        if breaker is not None and breaker != 'in':
            raise SyntaxError(
                'Correct syntax for loading modules into a custom '
                'variable is like so; {% load_modules as variable %}'
            )

        self.into_var = into_var

    def render(self, context):
        from pyalp_translation.customization import custom_gettext
        _ = custom_gettext('global')

        skin = context['skin']
        flags = context['flags']

        ALP_TOURNAMENT_MODE = context['ALP_TOURNAMENT_MODE']
        user = context['user']

        modules = ModuleManager()
        modulelist = skin.modulelist

        for key, modulelistitem in modulelist.items():
            if key == "mod_controlpanel" and not ALP_TOURNAMENT_MODE:
                # in this module,
                # different code displayed if logged in and if not.
                modules.add_module(
                    "controlpanel",
                    modulelistitem[0],
                    0,
                    _("cpanel"),
                    0,
                    "",
                    modulelistitem[1]
                )
            # elif key == "mod_register" and not ALP_TOURNAMENT_MODE:
            #     if not user.is_authenticated():
            #         # only displayed modules if not logged in.
            #         modules.add_module(
            #             "register",
            #             modulelistitem[0],
            #             0,
            #             "",
            #             1,
            #             "",
            #             modulelistitem[1]
            #         )
            elif key == "mod_admincontrolpanel":
                if user.is_staff:
                    modules.add_module(
                        "admincontrolpanel",
                        modulelistitem[0],
                        2,
                        _("administrator") + " " + _("cpanel"),
                        0,
                        "",
                        modulelistitem[1]
                    )
            elif key == "mod_guides":
                if user.is_staff:
                    modules.add_module(
                        "guides",
                        modulelistitem[0],
                        2,
                        _("admin_guides"),
                        0,
                        "",
                        modulelistitem[1]
                    )
            # elif key == "mod_schedule":
            #     if flags["schedule"]:
            #         modules.add_module(
            #             "schedule",
            #             modulelistitem[0],
            #             0,
            #             _("schedule_hour"),
            #             0,
            #             "",
            #             modulelistitem[1]
            #         )
            # elif key == "mod_tournaments" and not ALP_TOURNAMENT_MODE:
            #     modules.add_module(
            #         "tournaments",
            #         modulelistitem[0],
            #         0,
            #         _("tournaments"),
            #         0,
            #         "tournaments.php",
            #         modulelistitem[1]
            #     )
            # elif key == "mod_polls" and not ALP_TOURNAMENT_MODE:
            #     polls = Poll.objects.count()
            #     if polls:
            #         # only display module if there are polls in the database.
            #         modules.add_module(
            #             "polls",
            #             modulelistitem[0],
            #             0 if master['pollsguest'] else 1,
            #             _("polls"),
            #             0,
            #             "polls.php",
            #             modulelistitem[1]
            #         )

            # elif key == 'mod_news':
            #     news = NewsItem.objects.filter(hide_item=False).count()
            #     modules.add_module(
            #         "news",
            #         modulelistitem[0],
            #         0,
            #         _("announcements"),
            #         0,
            #         '',
            #         modulelistitem[1]
            #     )

        context['modules'] = modules

        from pprint import pprint
        print('main')
        pprint(modules.mainModules)

        print('left')
        pprint(modules.leftModules)

        print('right')
        pprint(modules.rightModules)

        return ''

from django import template
register = template.Library()
register.tag('load_modules', LoadModulesNode.invoke)
