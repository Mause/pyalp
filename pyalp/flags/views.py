from operator import attrgetter

from django.conf import settings
from django.core.context_processors import csrf
from pyalp.utils import render_to_response

from vanilla import CreateView
import floppyforms.forms

from flags.models import Flag
from flags.registry import get_flag_registry


class FlagsForm(floppyforms.forms.Form):
    if settings.ALP_TOURNAMENT_MODE:
        satellite = floppyforms.BooleanField(
            False,
            label='ALP satellites',
            help_text=''
        )

        benchmarks = floppyforms.BooleanField(
            False,
            label='benchmark competition',
            help_text=''
        )

        caffeine = floppyforms.BooleanField(
            False,
            label='caffeine log',
            help_text=''
        )

    if ((not settings.ALP_TOURNAMENT_MODE) or
            settings.ALP_TOURNAMENT_MODE_COMPUTER_GAMES):
        hlsw = floppyforms.BooleanField(
            False,
            label='HLSW server connects',
            help_text=''
        )

    if not settings.ALP_TOURNAMENT_MODE:
        uploading = floppyforms.BooleanField(
            False,
            label='file uploading',
            help_text=''
        )

        files = floppyforms.BooleanField(
            False,
            label='files',
            help_text=''
        )

        foodrun = floppyforms.BooleanField(
            False,
            label='food runs',
            help_text=''
        )

        pizza = floppyforms.BooleanField(
            False,
            label='pizza orders',
            help_text=''
        )

        gamerequests = floppyforms.BooleanField(
            False,
            label='game requests',
            help_text=''
        )

        servers = floppyforms.BooleanField(
            False,
            label='game servers',
            help_text=''
        )

        marath = floppyforms.BooleanField(
            False,
            label='the marathon',
            help_text=''
        )

        music = floppyforms.BooleanField(
            False,
            label='music jukebox',
            help_text=''
        )

    if not settings.ALP_TOURNAMENT_MODE:
        prizes = floppyforms.BooleanField(
            False,
            label='prize registration',
            help_text=''
        )

    schedule = floppyforms.BooleanField(
        False,
        label='schedule',
        help_text=''
    )

    if not settings.ALP_TOURNAMENT_MODE:
        seating = floppyforms.BooleanField(
            False,
            label='seating map',
            help_text=''
        )

        shoutbox = floppyforms.BooleanField(
            False,
            label='shoutbox',
            help_text=''
        )

    messaging = floppyforms.BooleanField(
        False,
        label='user messaging',
        help_text=''
    )

    currentattendance = floppyforms.BooleanField(
        False,
        label='sidebar module -- current attendance',
        help_text=''
    )

    if not settings.ALP_TOURNAMENT_MODE:
        filesharing = floppyforms.BooleanField(
            False,
            label='extra - file sharing info',
            help_text=''
        )

        gamerofthehour = floppyforms.BooleanField(
            False,
            label='extra - gamer of the hour',
            help_text=''
        )

        gamingrigs = floppyforms.BooleanField(
            False,
            label='extra - gaming rigs',
            help_text=''
        )

        policy = floppyforms.BooleanField(
            False,
            label='extra - policy',
            help_text=''
        )

        techsupport = floppyforms.BooleanField(
            False,
            label='extra - tech-support queue',
            help_text=''
        )

        timeremaining = floppyforms.BooleanField(
            False,
            label='extra - time remaining',
            help_text=''
        )

        staff = floppyforms.BooleanField(
            False,
            label='extra - staff page',
            help_text=''
        )

        sponsors = floppyforms.BooleanField(
            False,
            label='extra - sponsors',
            help_text=''
        )


class AdminToggleView(CreateView):
    def get(self, request):
        status_dict = get_flag_registry().get_statusdict()

        args = csrf(request)
        args['toggle_form'] = FlagsForm(status_dict).as_p()
        return render_to_response(
            'admin_toggle.html',
            args,
            context_instance=request
        )

    def post(self, request):
        toggle_form = FlagsForm(request.POST)
        if not toggle_form.is_valid():
            raise Exception()

        # modify existing flag objects
        flags = Flag.objects.all()
        for flag in flags:
            if flag.enabled != toggle_form.cleaned_data[flag.name]:
                flag.enabled = toggle_form.cleaned_data[flag.name]
                flag.save()

        # create new flag objects where necessary
        # one time op for most of the time
        initalized_flag_names = set(map(attrgetter('name'), flags))
        for name, val in toggle_form.cleaned_data.items():
            if name not in initalized_flag_names:
                Flag(name=name, enabled=val).save()

        return self.get(request)

    # @method_decorator(login_required)
    # @permission_required('flags.can_change_flags')
    # def dispatch(self, *args, **kwargs):
    #     return super(AdminToggleView, self).dispatch(*args, **kwargs)
