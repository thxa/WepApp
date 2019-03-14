from corsheaders.signals import check_request_enabled

from main.models import Season

def cors_allow_mysites(sender, request, **kwargs):
    return Season.objects.filter(host=request.host).exists()

check_request_enabled.connect(cors_allow_mysites)
