from operator import attrgetter

from django.conf import settings
from django.core.context_processors import csrf
from pyalp.utils import render_to_response

from vanilla import CreateView
import floppyforms.forms

from flags.models import Flag
from flags.registry import flag_registry


class FlagsForm(floppyforms.forms.Form):
    if settings.ALP_TOURNAMENT_MODE:
        satellite = floppyforms.BooleanField(False)
        satellite.label = 'ALP satellites'
        benchmarks = floppyforms.BooleanField(False)
        benchmarks.label = 'benchmark competition'
        caffeine = floppyforms.BooleanField(False)
        caffeine.label = 'caffeine log'

    if (not settings.ALP_TOURNAMENT_MODE) or settings.ALP_TOURNAMENT_MODE_COMPUTER_GAMES:
        hlsw = floppyforms.BooleanField(False)
        hlsw.label = 'HLSW server connects'

    if not settings.ALP_TOURNAMENT_MODE:
        uploading = floppyforms.BooleanField(False)
        uploading.label = 'file uploading'
        files = floppyforms.BooleanField(False)
        files.label = 'files'
        foodrun = floppyforms.BooleanField(False)
        foodrun.label = 'food runs'
        pizza = floppyforms.BooleanField(False)
        pizza.label = 'pizza orders'
        gamerequests = floppyforms.BooleanField(False)
        gamerequests.label = 'game requests'
        servers = floppyforms.BooleanField(False)
        servers.label = 'game servers'
        marath = floppyforms.BooleanField(False)
        marath.label = 'the marathon'
        music = floppyforms.BooleanField(False)
        music.label = 'music jukebox'

    if not settings.ALP_TOURNAMENT_MODE:
        prizes = floppyforms.BooleanField(False)
        prizes.label = 'prize registration'

    schedule = floppyforms.BooleanField(False)
    schedule.label = 'schedule'
    if not settings.ALP_TOURNAMENT_MODE:
        seating = floppyforms.BooleanField(False)
        seating.label = 'seating map'
        shoutbox = floppyforms.BooleanField(False)
        shoutbox.label = 'shoutbox'

    messaging = floppyforms.BooleanField(False)
    messaging.label = 'user messaging'
    currentattendance = floppyforms.BooleanField(False)
    currentattendance.label = 'sidebar module -- current attendance'
    if not settings.ALP_TOURNAMENT_MODE:
        filesharing = floppyforms.BooleanField(False)
        filesharing.label = 'extra - file sharing info'
        gamerofthehour = floppyforms.BooleanField(False)
        gamerofthehour.label = 'extra - gamer of the hour'
        gamingrigs = floppyforms.BooleanField(False)
        gamingrigs.label = 'extra - gaming rigs'
        policy = floppyforms.BooleanField(False)
        policy.label = 'extra - policy'
        techsupport = floppyforms.BooleanField(False)
        techsupport.label = 'extra - tech-support queue'
        timeremaining = floppyforms.BooleanField(False)
        timeremaining.label = 'extra - time remaining'
        staff = floppyforms.BooleanField(False)
        staff.label = 'extra - staff page'
        sponsors = floppyforms.BooleanField(False)
        sponsors.label = 'extra - sponsors'


class AdminToggleView(CreateView):
    def get(self, request):
        status_dict = flag_registry.get_statusdict()

        args = csrf(request)
        args['toggle_form'] = FlagsForm(status_dict).as_p()
        return render_to_response('admin_toggle.html', args)

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
