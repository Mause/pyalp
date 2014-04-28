from os.path import exists

from django.template.loader import render_to_string

from pyalp.skin import get_skin

from pyalp_page.templatetags.spacer import SpacerNode


class Module(object):
    # stores data for a single module
    # var _name, _loc, _str, _link, _sec, _isSlim, _isOpen, _type

    def __init__(self, n='', l='main', sec=1,
                 st='', sl=0, link='', module_type=''):
        # constructor
        self.name = n
        self.loc = l
        self.str = st
        self.link = link
        self.sec = sec
        self.isSlim = sl
        self.isOpen = 1
        self.module_type = module_type

        self.skin = get_skin()

    def display_module(self, overwrite=''):
        # global container
        var = self.current_security_level() >= self.get_security()
        if var:
            if overwrite:
                loc = overwrite
            else:
                if self.get_type() != "":
                    loc = self.get_type()
                else:
                    loc = self._loc

            return render_to_string('display_module.html', {'loc': loc})

    def get_inner_width(self):
        # global master, container
        if self.loc != 'main':
            sides = ['tl', 'tr', 'bl', 'br']
            # the dims array in this case only stores widths
            dims = {}
            for side in sides:
                key = 'mod' + side
                if exists(self.skin.skin_name + 'mod'+side+'.gif'):
                    temp = self.skin.getimagesize(
                        self.skin.skin_name + key + '.gif'
                    )
                    dims[key] = temp[0]
                else:
                    dims[key] = self.skin.container['border_width']

            extra = []
            if(dims['modtl'] > dims['modbl'] or dims['modtl'] > dims['modbl']):
                extra[0] = max(dims['modtl'], dims['modbl'])
            else:
                extra[0] = dims['modtl']

            if(dims['modtr'] > dims['modbr'] or dims['modtr'] > dims['modbr']):
                extra[1] = max(dims['modtr'], dims['modbr'])
            else:
                extra[1] = dims['modtr']

            return (
                self.skin.container[self.loc + 'module'] - 2 *
                self.skin.container['horizontalmodulepadding'] - extra[0] -
                extra[1] - 10) + 'px'
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

    def add_module(self, n='', l='', sec=0, st='', sl=0, link='', type=''):
        # adds a module to the manager
        mod = Module(n, l, sec, st, sl, link, type)

        if l == 'left':
            self.leftModules.append(mod)

        if l == 'right':
            self.rightModules.append(mod)

        if l == 'main':
            self.mainModules.append(mod)

    def display_all_modules(self, side):
        raise Exception('Use the appropriate method directly')

    def display_modules_right(self):
        return self.display_modules_for_side(
            self.rightModules,
            'right',
            self.skin.container['rightmodule']
        )

    def display_modules_main(self):
        return self.display_modules_for_side(
            self.mainModules,
            'main'
        )

    def display_modules_left(self):
        return self.display_modules_for_side(
            self.leftModules,
            'left',
            self.skin.container['leftmodule']
        )

    def display_modules_for_side(self, modules, side, width_modules=0):
        "displays all the modules for a side."

        if modules:
            types = {
                'left': 0,
                'right': 0,
                'main': 0
            }

            for mod in modules:
                types[mod.get_type()] += 1

            context = {
                'modules': self,
                'width_modules': width_modules
            }

            return render_to_string('display_all_modules.html', context)
        elif side != 'main':
            import pudb
            pudb.set_trace()
            node = SpacerNode.init_lit(
                self.skin.container['horizontalpadding']
            )
            return node.render({})
        else:
            return ''

    def get_width(self, side=None):
        if self.rightModules:
            right = (
                self.skin.container['rightmodule'] + 2 *
                self.skin.container['horizontalpadding']
            )
        else:
            right = self.skin.container['horizontalpadding']

        if self.leftModules:
            left = (
                self.skin.container['leftmodule'] + 2 *
                self.skin.container['horizontalpadding']
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
