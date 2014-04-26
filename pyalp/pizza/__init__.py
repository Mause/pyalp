from pizza import flags
flags.register_flags()

from pyalp_translation.customization import custom_gettext
gettext = custom_gettext('pizza')
