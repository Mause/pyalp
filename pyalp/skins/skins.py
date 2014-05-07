from os.path import join, exists, basename

from PIL import Image

from pyalp.config import get_config

from pyalp.map import tree


class Skin(object):
    tree = list(tree)

    def __init__(self):
        self.config = get_config()

        self.skin_name = self.config.skin['skin_name']

        self.asset_path = self.config.skin['skin_path']
        assert exists(self.asset_path)

    @property
    def colors(self):
        return self.config.skin['colors']

    @property
    def container(self):
        return self.config.skin['container']

    @property
    def modulelist(self):
        return self.config.modulelist

    @property
    def images(self):
        if exists(join(self.asset_path, 'img')):
            prefix = 'img'
        else:
            prefix = ''

        return {
            key: join(prefix, val)
            for key, val in self.config.skin['images'].items()
        }

    def mini_menu(self):
        menu = []
        filename = basename(__file__)
        save = -1
        i = 0

        while self.tree and (self.tree[i] if len(self.tree) > i else False) and save == -1:
            if self.tree[i][1] == filename:
                save = i
            i += 1

        if save > -1:
            menu.append(save)
            temp = self.tree[save][2]

            while temp != -1:
                oldtemp = temp
                menu.append(oldtemp)
                temp = self.tree[oldtemp][2]

        string = ""
        i = len(menu) - 1
        while i >= 0:
            if self.tree[menu[i]][1]:
                string += '<a href="{}" class="menu">'.format(
                    self.tree[menu[i]][1]
                )

            string += self.tree[menu[i]][0]

            if not self.tree[menu[i]][1]:
                string += "</a>"

            if i != 0:
                string += " &gt; "

            i -= 1

        return string

    def getimagesize(self, path):
        return Image.open(path).size
