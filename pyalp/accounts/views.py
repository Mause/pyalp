from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from pyalp.utils import render_to_response

from .models import UserMetadata
from apps.techsupport.models import TechSupportRequest

from pyalp_translation.customization import custom_gettext
_ = custom_gettext('login')


class LoginForm(forms.Form):
    username = forms.CharField(
        label=_('username'),
        error_messages={
            'required': _('blank_user')
        }
    )

    password = forms.CharField(
        label=_('password'),
        widget=forms.PasswordInput,
        error_messages={
            'required': _('blank_pass')
        }
    )


def login_view(request):
    referer = request.GET.get('ref')

    if request.user.is_authenticated():
        return redirect(referer or '/')

    f = LoginForm(request.POST)
    if request.POST and f.is_valid():
        cleaned = f.clean()

        username = cleaned.get('username')
        password = cleaned.get('password')
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect(referer or '/')

        else:
            f._errors.setdefault(
                "__all__",
                forms.util.ErrorList()
            )
            f._errors["__all__"].append(
                _('bad_pass') + ' ' +
                _('bad_user')
            )

    elif not request.POST:
        # page directly accessed, no login information
        # submitted
        f.data = {}
        f.errors.clear()

    print(request.POST)

    return render_to_response(
        'login.html',
        {'login_form': f},
        context_instance=request
    )


def logout_view(request):
    logout(request)
    return redirect('/')


def users(request):
    return render_to_response(
        'users.html',
        context_instance=request
    )


def single_user(request, user_id):
    try:
        # if we do it this way we got both models in one query
        user_meta = UserMetadata.objects.select_related('user')
        user_meta = user_meta.get(user_id=user_id)
        user_to_display = user_meta.user
    except UserMetadata.DoesNotExist:
        user_to_display, user_meta, tech = None, None, None

    # tsq = tech support requests
    requests_made = TechSupportRequest.objects.filter(
        user=user_to_display
    ).count()
    requests_solved = TechSupportRequest.objects.filter(
        fixer=user_to_display
    ).count()

    context = {
        'user_to_display': user_to_display,
        'metadata': user_meta,
        'requests_solved': requests_solved,
        'requests_made': requests_made
    }

    return render_to_response(
        'single_user.html',
        context,
        context_instance=request
    )
