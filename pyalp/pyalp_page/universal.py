from collections import namedtuple

from django.template import render_to_string

from pyalp_page.module import start_module, end_module
from pyalp_translation.customization import trans_standalone

# require_once '_config.php'
# require_once 'include/_functions.php'
# require_once 'include/_includes.php'

# URL_handler = new URL_handler()


class Form(object):
    pass


SecurityEnum = type('SecurityEnum', (object,), {
    "SUPERADMIN": 3,
    "ADMIN": 2,
    "USER": 1,
    "GUEST": 0
})


class UniversalView(Form):
    # _name, _singular
    # _table_name, _id, _order
    _permissions = []        # which options to display to user.
    _notes = []              # notes to display to user
    _extra = []              # extra sql statements to run

    # @_crutch
    # if the crutch is true,
    # some elements become unmodifiable.
    # (must be the name of a column in the table)

    #_print
    _related_links = []
    _delmod_query = None

    def __init__(self, name, singular, security):
        """
        @security
            level 3: super admin only
            level 2: admins+
            level 1: users+
            level 0: guests+
        """

        self._name = name
        self._singular = singular
        self._security = security

        self._table_name = ''
        self._id = ''
        self._order = ''

        self._permissions['add'] = 0
        self._permissions['del'] = 0
        self._permissions['mod'] = 0
        self._permissions['update'] = 0

        # initialize optional variables.
        self._notes['add'] = ''
        self._notes['del'] = ''
        self._notes['mod'] = ''
        self._notes['update'] = ''
        self._print = []
        self._related_links = []
        self._crutch = 0
        self._delmod_query = ''

    def _(self, const):
        return trans_standalone({}, const)

    def database(self, table, id, order):
        self._table_name = table
        self._id = id
        self._order = order

    def permissions(self, type, value):
        self._permissions[type] = value

    def add_extra(self, type, array):
        self._extra[type] = array

    def add_notes(self, type, note):
        self._notes[type] = note

    def add_crutch(self, crutch):
        self._crutch = crutch

    """
    def add_print(print)
        self._print = print
    """

    def add_delmod_query(self, query):
        self._delmod_query = query

    def start_elements(self):
        # call after adding crutch and before adding elements.
        self.form(self._crutch)

    def get_name(self):
        return self._name

    def get_singular(self):
        return self._singular

    def is_secure(self):
        if self.current_security_level() >= self._security:
            return True
        else:
            return False

    # display functions
    def display(self):
        # global lang, master, toggle, lan, colors, images, start,
        # end, container, modules, dims
        if(self.method != "POST" and self.is_secure()):
            self.display_top()
            self.display_form()
            self.display_bottom()
        elif (self.method == "POST" and self.is_secure()):
            self.display_results()
        else:
            self.display_slim('you are not authorized to view this page.')

    RelatedLink = namedtuple('RelatedLink', 'name,url,security')

    def add_related_link(self, name, url, security):
        self._related_links.append(
            self.RelatedLink(name, url, security)
        )

    def display_related_links(self):
        # global lang, images
        html = ''

        if self._related_links:
            to_display = filter(
                lambda val: self.current_security_level() >= val.security
            )

            if to_display:
                html += (
                    '<font class="sm"><strong>related links</strong> //<br />'
                )

                for val in to_display:
                    html += '&nbsp;' + self.skin.get_arrow()
                    html += '&nbsp;<a href="' + val.url + '">'

                    if val.security > SecurityEnum.ADMIN:
                        html += "<strong>super </strong>"

                    if val.security > SecurityEnum.USER:
                        html += '<strong>administrator</strong>: '

                    html += val.name
                    html += '</a><br /><?php'

                html += '</font><br />'

        return html

    def display_top(self, modjool=True, side=True):
        # global lang, master, toggle, lan, colors, images, start, end,
        # container, modules, dims
        if (self._security == SecurityEnum.SUPERADMIN):
            title = self._("sadministrator") + ': ' + self._name
        elif (self._security == SecurityEnum.ADMIN):
            title = self._("administrator") + ': ' + self._name
        else:
            title = self._name

        context = {
            'title': title
        }

        if side:
            html = render_to_string('include/_top.php', context)
        else:
            html = render_to_string('include/_top_noside.php', context)

        if modjool:
            html += start_module()

        return html

    def display_form(self):
        # global lang, master, toggle, lan, colors, images, start, end,
        # container, modules, dims, URL_handler

        html = ''

        # if post is empty, this is displayed.
        if self._security == SecurityEnum.SUPERADMIN:
            html += "<strong>" + self._("sadministrator")
            html += "</strong>:  " + self._name
        elif self._security == SecurityEnum.ADMIN:
            html += "<strong>" + self._("administrator")
            html += "</strong>:  " + self._name
        else:
            html += '<strong>' + self._name + '</strong>:'

        if self.request.GET['mod'] and self.request.GET['q']:
            html += '<span class="sm pyalp-blended-text">'

            # <?php echo get_script_name(); ?>
            html += '[<a href="#">back to all ' + self._name + '</a>]</span>'

        html += '<br /><br />'
        self.display_related_links()

        if any(self._permissions.values()):
            if any([self._table_name, self._id, self._order]):
                html += render_to_string('include/_universal_nopost.php')
            else:
                html += (
                    "the script has no database table information to work "
                    "with. don't forget to call the database function from "
                    "your script.<br /><br />"
                )
        else:
            html += (
                "the script has no permissions available. "
                "don't forget to call the permissions function"
                "from your script.<br /><br />"
            )
        return html

    def display_bottom(modjool=True, side=True):
        # global lang, master, toggle, lan, colors, images, start, end,
        # container, modules, dims
        if modjool:
            end_module()

        if side:
            return render_to_string('include/_bot.php')
        else:
            return render_to_string('include/_bot_noside.php')

    def display_results(self, redirect=''):
        # global lang, master, toggle, lan, colors, images, start, end,
        # container, modules, dims, URL_handler

        # if post is not empty, this is displayed.
        # WARNING: does not use display_top and display_bottom.
        if any([self._table_name, self._id, self._order]):
            html = render_to_string('include/_universal_post.php')
        else:
            html = self.display_top()
            html += (
                "the script has no database table information to work with. "
                "don't forget to call the database function.<br /><br />"
            )
            html += self.display_bottom()
        return html

    def display_slim(string, redirect='index.php', redirect_time=2):
        raise Exception('avoid this function please')
        # # global lang, master, toggle, lan, colors, images, start, end
        # if stristr(string, 'success'):
        #     self.set_header('Location', redirect)

        # elif stristr(string, 'you are not authorized to view this page.') and
        # self.current_security_level()==0:
        #     title = self._name
        #     redirect = 'login.php?ref=' + urlencode(
            # basename(get_script_name()))
        #     include 'include/_top_slim.php'; ?>
        #     <br /><a href="<?php echo redirect; ?>" class="radio"><strong>
        # <?php echo string; ?> &nbsp;redirect in <span id="pendule"></span>
        # &nbsp;seconds.</strong></a><br /><br />
        #     <?php
        #     include 'include/_bot_slim.php'
        # else:
        #     title = self._name
        #     include 'include/_top_slim.php'; ?>
        #     <br /><a href="<?php echo redirect; ?>" class="radio"><strong>
        # <?php echo string; ?> &nbsp;redirect in <span id="pendule"></span>
        # &nbsp;seconds.</strong></a><br /><br />
        #     <?php
        #     include 'include/_bot_slim.php'
        # }

    def display_smallwindow_top(bg_override='', nomargin=0):
        # global lang, master, toggle, lan, colors, images, start, end,
        # container, modules, dims
        return render_to_string('include/_top_smallwindow.php')

    def display_smallwindow_bottom():
        # global lang, master, toggle, lan, colors, images, start, end,
        # container, modules, dims
        return render_to_string('include/_bot_smallwindow.php')
