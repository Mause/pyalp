from os.path import exists, join

from pyalp.skin import get_skin


class Module(object):
    "stores data for a single module"

    def __init__(
            self, name='', loc='main', security_level=1,
            string='', isSlim=False, link='', module_type=''):
        self.name = name
        self.loc = loc
        self.string = string
        self.link = link
        self.security_level = security_level
        self.isSlim = isSlim
        self.isOpen = True
        self.module_type = module_type

        self.skin = get_skin()

    # display_module got re-implemented as template tag

    def get_inner_width(self):
        if self.loc != 'main':
            sides = ['tl', 'tr', 'bl', 'br']

            # the dims array in this case only stores widths
            dims = {}
            for side in sides:
                key = 'mod' + side

                path = join(
                    self.skin.asset_path, 'img', key + '.gif'
                )

                if exists(path):
                    width, _ = self.skin.getimagesize(path)
                    dims[key] = width
                else:
                    dims[key] = self.skin.container['border_width']

            extra = []
            if dims['modtl'] > dims['modbl'] or dims['modtl'] > dims['modbl']:
                extra.append(max(dims['modtl'], dims['modbl']))
            else:
                extra.append(dims['modtl'])

            if dims['modtr'] > dims['modbr'] or dims['modtr'] > dims['modbr']:
                extra.append(max(dims['modtr'], dims['modbr']))
            else:
                extra.append(dims['modtr'])

            px = (
                self.skin.container[self.loc + 'module'] - 2 *
                self.skin.container['horizontalmodulepadding'] - extra[0] -
                extra[1] - 10
            )
            return '{}px'.format(px)
        else:
            return '96%'

    def is_module_secure(self):
        return (self.current_security_level() >= self.get_security())


class ModuleManager(object):
    """
    manages a collection of modules
    """

    def __init__(self):
        self.leftModules = []
        self.rightModules = []
        self.mainModules = []

        self.skin = get_skin()

    def add_module(
            self, name='', loc='', security_level=0,
            string='', isSlim=0, link='', module_type=''):
        "adds a module to the manager"
        mod = Module(
            name,
            loc,
            security_level,
            string,
            isSlim,
            link,
            module_type
        )

        if loc == 'left':
            self.leftModules.append(mod)

        elif loc == 'right':
            self.rightModules.append(mod)

        elif loc == 'main':
            self.mainModules.append(mod)

        else:
            raise Exception('Invalid location {}'.format(loc))

    def get_width(self, side=None):
        if self.rightModules:
            right = (
                self.skin.container['rightmodule'] +
                2 * self.skin.container['horizontalpadding']
            )
        else:
            right = self.skin.container['horizontalpadding']

        if self.leftModules:
            left = (
                self.skin.container['leftmodule'] +
                2 * self.skin.container['horizontalpadding']
            )
        else:
            left = self.skin.container['horizontalpadding']

        output = {
            'right': right,
            'left': left
        }

        # for templating reasons
        if side:
            return output[side]
        else:
            return output
