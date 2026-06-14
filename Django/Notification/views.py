from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Notification, NotificationRead
from .serializers import NotificationSerializer


@api_view(['GET'])
def notification_list(request):
    """
    GET /api/notifications/?token=<client_token>&since=<id>
    Returns active notifications the client has NOT yet read.
    Optional `since` param: only return notifications newer than that id
    (used for polling — avoids re-fetching everything every time).
    """
    token = request.query_params.get('token', '').strip()
    since = request.query_params.get('since', None)

    if not token:
        return Response({'error': 'توکن الزامی است'}, status=status.HTTP_400_BAD_REQUEST)

    qs = Notification.objects.filter(is_active=True)

    if since:
        try:
            qs = qs.filter(id__gt=int(since))
        except (ValueError, TypeError):
            pass

    # Exclude notifications this token already read
    read_ids = NotificationRead.objects.filter(
        client_token=token
    ).values_list('notification_id', flat=True)

    qs = qs.exclude(id__in=read_ids).order_by('-created_at')

    serializer = NotificationSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def mark_notifications_read(request):
    """
    POST /api/notifications/mark-read/
    Body: { "token": "<client_token>", "ids": [1, 2, 3] }
    Marks the given notification IDs as read for this token.
    """
    token = request.data.get('token', '').strip()
    ids   = request.data.get('ids', [])

    if not token:
        return Response({'error': 'توکن الزامی است'}, status=status.HTTP_400_BAD_REQUEST)

    if not isinstance(ids, list) or not ids:
        return Response({'error': 'آیدی‌های اعلان الزامی است'}, status=status.HTTP_400_BAD_REQUEST)

    notifications = Notification.objects.filter(id__in=ids, is_active=True)
    created = 0
    for notif in notifications:
        _, was_created = NotificationRead.objects.get_or_create(
            notification=notif,
            client_token=token,
        )
        if was_created:
            created += 1

    return Response({'marked': created})
