from django.shortcuts import render
from notification.models import Notification

# Create your views here.
def notification_view(request):
    notifications = Notification.objects.filter(receiver=request.user)
    new_notifications = []
    notifications_count = 0
    for notify in notifications:
        if notify.notify_flag == False:
            notifications_count += 1
            new_notifications.append(notify.msg_content)
            notify.notify_flag = True
            notify.save()
    return render(request, 'notifications.html', {"new_notifications": new_notifications, "notifications_count": notifications_count})

