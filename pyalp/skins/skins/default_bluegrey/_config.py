def config(vars):
    # IF YOU ARE MAKING A CUSTOM SKIN, PLEASE INCLUDE WHAT VERSION OF ALP IT
    # WAS MADE FOR.
    # ie: this custom skin was made for ALP 0.97.2d

    # colors (can also accept standard html name colors such as pink or green)
    colors = {
        'background': '#2D2D3A',
        'primary': '#E8860C',
        'secondary': '#804F01',
        'border': '#4C4D5C',

        # currently only used on bargraph borders
        'border_alternate': '#181821',

        'cell_title': '#595B68',
        'cell_background': '#2D2D3A',
        'cell_alternate': '#282832',
        'text': '#9999AC',
        'blended_text': '#767A8A',
        'alert': '#ff0000',

        'image_text': 'white'  # ONLY white or black
    }
    colors['graphs'] = colors['primary']

    # images
    images = {
        'background': '',
        'title': 'title.gif',
        'arrow_on': 'phpwcms_arrow_off.gif',
        'arrow_off': 'phpwcms_arrow.gif',
        'dotted_line': 'dotted_line.gif',
        'empty_bargraph_background': '/static/emptybargraphbg.gif',
        'go': 'white_go.gif'
    }

    # widths of right and left columns
    container = {}
    container['leftmodule'] = 200
    container['rightmodule'] = 200
    container['indexmodule'] = 250

    # padding (spacing inbetween modules and columns)
    container['horizontalpadding'] = 10
    container['verticalpadding'] = 10

    # module padding (spacing inside the module between content and border)
    container['horizontalmodulepadding'] = 8
    container['verticalmodulepadding'] = 3

    # border size: these are used only if mod****.gif images do not exist in
    # the current skin directory
    container['border_width'] = 1
    container['border_height'] = 1

    # seating chart colors
    seat = {}
    seat['background'] = colors['background']  # '#555555'
    seat['border'] = '#FFFFFF'
    seat['tablecolor'] = colors['secondary']
    seat['tableborder'] = colors['primary']
    seat['voidcolor'] = colors['cell_title']  # colors['cell_background']
    seat['gridcolor'] = '#CCCCCC'
    seat['currentcolor'] = colors['primary']
    seat['occupied'] = colors['text']
    seat['reserved'] = '#FF9900'

    # display title menu items on the left, right, or center.
    container['title_menu'] = 'left'

    # display index.php modules on left or right of body.
    container['index_modules'] = 'right'

    # these are the modules displayed.  if you delete a module from below, it will
    # not show up on ALP. this also controls the order of the modules.

    # array(location, type)
    # location options: 'left', 'right', or 'main'
    # type options: 'left', 'right', or 'main'
    modulelist = {
        'mod_controlpanel': ['left', 'main'],
        'mod_register': ['left', 'main'],
        'mod_admincontrolpanel': ['left', 'main'],
        'mod_guides': ['left', 'main'],
        'mod_schedule': ['left', 'main'],
        'mod_tournaments': ['left', 'main'],
        'mod_polls': ['left', 'main'],
    }

    if vars['ALP_TOURNAMENT_MODE']:
        modulelist['mod_news'] = ['left', 'main']

    return {
        'modulelist': modulelist,
        'skin': {
            'colors': colors,
            'images': images,
            'container': container
        },
    }
