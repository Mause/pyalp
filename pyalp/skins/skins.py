from os.path import join, exists, basename

from PIL import Image
from django.template.loader import render_to_string

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
    def images(self):
        return {
            key: 'img/' + val
            for key, val in config.skin['images'].items()
        }

    def get_arrow(self, type='off'):
        tempurl = self.images['arrow_' + type]

        width, height = self.getimagesize(
            join(self.asset_path, tempurl)
        )

        context = {'tempurl': tempurl, 'width': width, 'height': height}
        return render_to_string('arrow.html', context)

    def get_go(self, url):
        tempurl = self.images['go']
        width, height = self.getimagesize(tempurl)

        go = """
        &nbsp; \
        <a href="{url}">
            <img \
                src="{tempurl}" \
                width="{width}" \
                height="{height}" \
                border="0" \
                alt="go" \
                align="absmiddle" \
            />
        </a>
        """.format(url=url, tempurl=tempurl, width=width, height=height)
        return go

    def mini_menu(self):
        # global tree
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
