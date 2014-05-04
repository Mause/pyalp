

def config(vars):
    # IF YOU ARE MAKING A CUSTOM SKIN,
    # PLEASE INCLUDE WHAT VERSION OF ALP IT WAS MADE FOR.
    # ie: this custom skin was made for ALP 0.97.2d

    # colors (can also accept standard html name colors such as pink or green)
    colors = {
        'background': '#4C5844',
        'primary': '#BEAD45',
        'secondary': '#000000',
        'border': '#2C3329',

        # currently only used on bargraph borders
        'border_alternate': '#20241E',

        'cell_title': '#2C3329',
        'cell_background': '#2C3329',
        'cell_alternate': '#272B25',
        'text': '#A0AA95',
        'blended_text': '#000000',
        'alert': '#ff0000',
        'image_text': 'white'  # ONLY white or black,
    }
    colors['graphs'] = colors['primary']

    # images
    images = {
        'background': '',
        'title': 'title.gif',
        'arrow_on': 'phpwcms_arrow_off.gif',
        'arrow_off': 'phpwcms_arrow.gif',
        'dotted_line': 'dotted_line.gif',
        'empty_bargraph_background': 'emptybargraphbg.gif',
        'go': 'white_go.gif',
    }

    # widths of right and left columns
    container = {
        'leftmodule': 210,
        'rightmodule': 200,
        'indexmodule': 250,

        # padding (spacing inbetween modules and columns)
        'horizontalpadding': 4,
        'verticalpadding': 0,

        # module padding (spacing inside the module between content and border)
        'horizontalmodulepadding': 1,
        'verticalmodulepadding': 3,

        # border size: these are used only if mod****.gif images do not exist
        # in the current skin directory
        'border_width': 1,
        'border_height': 1,

        # display title menu items on the left, right, or center.
        'title_menu': 'left',
    }

    # seating chart colors
    seat = {}
    seat['background'] = colors['background']  # '#555555'
    seat['border'] = '#FFFFFF'
    seat['tablecolor'] = colors['secondary']
    seat['tableborder'] = colors['primary']
    seat['voidcolor'] = colors['cell_title']  # colors['cell_background']
    seat['gridcolor'] = '#CCCCCC'
    seat['currentcolor'] = colors['primary']
    seat['occupied'] = '#007700'
    seat['reserved'] = '#FF9900'

    # display index.php modules on left or right of body.
    container['index_modules'] = 'right'

    # these are the modules displayed.  if you delete a module from below,
    # it will not show up on ALP.
    # this also controls the order of the modules.

    # array(location, type)
    # location options: 'left', 'right', or 'main'
    # type options: 'left', 'right', or 'main'
    modulelist = {}
    modulelist['mod_controlpanel'] = ['left', 'main']
    modulelist['mod_register'] = ['left', 'main']
    modulelist['mod_admincontrolpanel'] = ['left', 'main']
    modulelist['mod_guides'] = ['left', 'main']
    if vars['ALP_TOURNAMENT_MODE']:
        modulelist['mod_news'] = ['left', 'main']
    modulelist['mod_schedule'] = ['left', 'main']
    modulelist['mod_tournaments'] = ['left', 'main']
    modulelist['mod_polls'] = ['left', 'main']

    return {
        'modulelist': modulelist,
        'skin': {
            'colors': colors,
            'container': container,
            'images': images
        }
    }
