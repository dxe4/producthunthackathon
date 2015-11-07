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

    for i in range(0, 1):
        events = []
        params = {'page': 20}
        headers = {}

        if last_event:
            pass

        result = meetup.my_events(
            user_info.access_token, headers=headers, params=params
        )
        for item in result:
            if item.get("status") != 'past':
                continue
            else:
                data = {
                    'urlname': item.get('group', {}).get("urlname"),
                    'time': timestamp_to_datetime(item.get("time") / 1000),
                    'user': user,
                }
                data.update({key: item.get(key) for key in event_attrs})
                new_event = AttendedEvent(**data)
                events.append(new_event)

        AttendedEvent.objects.bulk_create(events)
