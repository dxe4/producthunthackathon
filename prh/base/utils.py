import datetime
import types

from django.conf import settings
import requests
import pytz


class MeetupOAuthExpcetion(Exception):
    pass


def timestamp_to_datetime(ts, safe=True):
    if safe and not ts:
        # unpythonic?
        return None

    return datetime.datetime.fromtimestamp(int(ts))


def utc_now():
    date = datetime.datetime.now()
    date = date.replace(tzinfo=pytz.utc)
    return date


class Meetup(object):
    authorize_url = "https://secure.meetup.com/oauth2/access"
    me_url = "https://api.meetup.com/2/member/self/"
    refresh_access_token_url = "https://secure.meetup.com/oauth2/access"
    my_events_url = "https://secure.meetup.com/self/events"

    def __init__(self, user_info=None):
        self.user_info = user_info
        self._update_info(user_info)

    def _update_info(self, user_info):
        if not user_info:
            return

        if not self._is_expired(self, user_info.expiry_time):
            return

        result = self.refresh_access_token(
            user_info.refresh_token
        )

        user_info.expires_in = timestamp_to_datetime(
            result.get('expires_in')
        )
        user_info.access_token = result['access_token']
        user_info.save()

    def _is_expired(self, expiry_time):
        dt = utc_now() - expiry_time
        if dt.seconds < 15:
            return True
        else:
            return False

    def get_refresh_token(self, code):
        '''
            return {
                access_token: xxxx,
                token_type: bearer,
                expires_in: 3600, (seconds)
                refresh_token: xxxxx
            }
        '''
        data = {
            'grant_type': 'authorization_code',
            'client_id': settings.MEETUP_CONSUMER_KEY,
            'client_secret': settings.MEETUP_CONSUMER_SECRET,
            'redirect_uri': settings.MEETUP_REDIRECT_URI,
            'code': code,
        }
        response = requests.post(self.authorize_url, data)
        if response.status_code is not 200:
            raise MeetupOAuthExpcetion("Opps something went wrong {}".format(
                response.status_code)
            )
        else:
            return response.json()

    def get_my_details(self, access_token):
        headers = {
            'Authorization': 'Bearer {}'.format(
                access_token
            )
        }

        details_result = requests.get(
            "https://api.meetup.com/2/member/self/", headers=headers
        )
        return details_result.json()

    def refresh_access_token(self, refresh_token):
        '''
            return {
              "access_token": xxxx,
              "token_type": "bearer",
              "expires_in":3600, seconds
              "refresh_token": xxxx
            }
        '''

        data = {
            'client_id': settings.MEETUP_CONSUMER_KEY,
            'client_secret': settings.MEETUP_CONSUMER_SECRET,
            'refresh_token': refresh_token,
            'grant_type': 'refresh_token'
        }
        result = requests.post(self.refresh_access_token_url, data=data)
        return result.json()

    def my_events(self, refresh_token, params, headers):
        result = requests.get(self.my_events_url, params=params)
        return result.json()


def meetup_signup(code):
    meetup = Meetup()
    authorization = meetup.get_refresh_token(code)
    my_details = meetup.refresh_access_token(
        refresh_token=authorization['refresh_token']
    )

    return {
        'auth': authorization,
        'me': my_details
    }
