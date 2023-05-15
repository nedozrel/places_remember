from django.conf import settings

def yandex_api(request):
    """
    Returns the Yandex.Maps API key for use in a template.

    :param request: the request object
    :return: a dictionary with the key `YANDEX_MAPS_API_KEY`, containing the Yandex.Maps API key
    """
    return {'YANDEX_MAPS_API_KEY': settings.YANDEX_MAPS_API_KEY}
