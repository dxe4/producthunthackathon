# normally would be a celery thing

import time
from urlparse import urlparse, parse_qs

from django.contrib.auth.models import User

from base.utils import Meetup, timestamp_to_datetime
from base.models import AttendedEvent

event_attrs = ['link', 'name', 'yes_rsvp_count']


def fetch_past_events(user_id):
    user = User.objects.get(pk=user_id)
    user_info = user.userinfo
    meetup = Meetup(user_info=user_info)
    last_event = None
    page = 20
    offset = 1
    meetup_ids = []

    while True:
        events = []
        params = {'page': page, 'offset': offset}
        headers = {}

        if last_event:
            pass

        response = meetup.my_events(
            user_info.access_token, headers=headers, params=params
        )
        link_header = response.links.get("next")

        if not link_header:
            break
        else:
            link_params = parse_qs(urlparse(link_header['url']).query)
            page = int(link_params['page'][0])
            offset = int(link_params['offset'][0])

        rate_limit = response.headers['X-RateLimit-Limit']
        if rate_limit < 2:
            time.sleep(response.headers['X-RateLimit-Reset'] + 1)

        for item in response.json():
            if item.get("status") != 'past':
                continue
            else:
                data = {
                    'urlname': item.get('group', {}).get("urlname"),
                    'time': timestamp_to_datetime(item.get("time") / 1000),
                    'user': user,
                    'meetup_id': item.get("id")
                }

                meetup_id = item.get("id")
                if meetup_id not in meetup_ids:
                    meetup_ids.append(meetup_id)
                else:
                    continue

                data.update({key: item.get(key) for key in event_attrs})
                new_event = AttendedEvent(**data)
                events.append(new_event)

        AttendedEvent.objects.bulk_create(events)
