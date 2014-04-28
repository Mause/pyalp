from flags.models import Flag


class NoSuchFlag(Exception):
    pass


class FlagRegistry(object):
    """
    Anything that any other add wants to do with flags should go
    through this registry
    """
    def __init__(self):
        self.defaults = {}
        self.flags = {}

    def is_flag_enabled(self, flag_name):
        if flag_name in self.flags:
            return self.flags[flag_name]
        elif flag_name in self.defaults:
            return self.defaults[flag_name]
        else:
            raise NoSuchFlag(flag_name)

        # flags = Flag.objects.filter(name=flag_name)
        # if len(flags) > 1:
        #     raise Exception('duplicate')

        # if not flags:
        #     raise NoSuchFlag(flag_name)
        # else:
        #     return flags[0].enabled

    def add_flag(self, name, default=False):
        self.defaults[name] = default
        self.flags[name] = None

    def add_flag_condition(self, to_add_add):
        pass

    def get_statusdict(self):
        return {
            flag.name: flag.enabled
            for flag in Flag.objects.all()
        }


# the FlagRegistry is essentially a singleton :)

def get_flag_registry():
    if not hasattr(get_flag_registry, 'flag_registry'):
        get_flag_registry.flag_registry = FlagRegistry()

    return get_flag_registry.flag_registry
