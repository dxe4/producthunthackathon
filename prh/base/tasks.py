# normally would be a celery thing

from django.contrib.auth.models import User

from base.utils import Meetup, timestamp_to_datetime
from base.models import AttendedEvent

event_attrs = ['link', 'name', 'yes_rsvp_count']


def fetch_past_events(user_id):
    user = User.objects.get(pk=user_id)
    user_info = user.userinfo
    meetup = Meetup(user_info=user_info)
    last_event = None

    for i in range(0, 10):
        events = []
        params = {}
        headers = {}

        if last_event:
            pass

        result = meetup.my_events(user_info.refresh_token)
        for k, v in result.items():
            if result.get("status") != 'past':
                continue
            else:
                data = {
                    'urlname': result.get('group', {}).get("urlname"),
                    'time': timestamp_to_datetime(result.get("time")),
                    'user': user,
                }
                data.update({key: result.get(key) for key in event_attrs})
                new_event = AttendedEvent(**data)
                events.append(new_event)

        AttendedEvent.objects.bulk_create(events)
