from django.conf import settings


def common_vars(request):
    result = {
        "MEETUP_REDIRECT_URI": settings.MEETUP_REDIRECT_URI,
    }

    return result
