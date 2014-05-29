# from django.shortcuts import render_to_response
from pyalp.utils import render_to_response
from .models import TechSupportRequest

# Create your views here.
from vanilla import View


class TechSupportRequestView(View):
    def get(self, request):
        queue = TechSupportRequest.objects.all().order_by('itemtime')

        assigned_to_current_user = TechSupportRequest.objects.filter(
            assigned_to=request.user
        )
        assigned_to_current_user_not_fixed = assigned_to_current_user.filter(
            fixed=False
        )
        assigned_to_current_user_fixed = assigned_to_current_user.filter(
            fixed=True
        )

        created_by_user = TechSupportRequest.objects.filter(user=request.user)
        created_by_user_unfixed = created_by_user.filter(fixed=False).order_by('itemtime')

        context = {
            'queue': queue,
            'assigned_to_current_user': assigned_to_current_user,
            'assigned_to_current_user_not_fixed': (
                assigned_to_current_user_not_fixed
            ),
            'assigned_to_current_user_fixed': assigned_to_current_user_fixed,
            'created_by_user_unfixed': created_by_user_unfixed
        }

        return render_to_response(
            'techsupport_get.html',
            context,
            context_instance=request
        )


def details(request, sid):
    tr = TechSupportRequest.objects.filter(id=sid)

    tr = tr[0] if tr else None

    return render_to_response(
        'techsupport_details.html',
        {'techsupport_request': tr},
        context_instance=request
    )
