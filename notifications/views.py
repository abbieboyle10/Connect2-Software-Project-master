from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Notification


def notifications(request):
    goto = request.GET.get('goto', '')
    notification_id = request.GET.get('notification', 0)
    extra_id = request.GET.get('extra_id', 0)

    if goto != '':
        notification = Notification.objects.get(pk=notification_id)
        job = notification.job
        notification.is_read = True
        notification.save()

        if notification.notification_type == Notification.MESSAGE:
            return redirect('view_application', id=notification.extra_id, pk=job.pk)
        elif notification.notification_type == Notification.APPLICATION:
            return redirect('jobprofile', pk=job.pk)

    return render(request, 'employer/noti.html')
