from skins import Skin


def get_skin():
    if not hasattr(get_skin, 'skin'):
        get_skin.skin = Skin()

    return get_skin.skin
