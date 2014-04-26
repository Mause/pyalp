from django.contrib import admin

from flags.models import Flag

FLAGS = ['pizza_orders']


class FlagsAdmin(admin.ModelAdmin):
    pass
    # def __init__(self, model, admin_site):
    #     self.model = model  # we don't really give a shit about this
    #     self.admin_site = admin_site

    # def admin_view(self):
    #     import pudb
    #     pu.db

    # def __getattr__(self, name):
    #     print('#####', name)
    #     return getattr(super(FlagsView, self), name)

    # def index(self):
    #     import pudb
    #     pu.db
    #     pass

admin.site.register(Flag, FlagsAdmin)
