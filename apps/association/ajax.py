from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
from .models import Device
import json



@csrf_exempt
@require_http_methods(['POST'])
def save_token(request):
    body = request.body.decode('utf-8')
    bodyDict = json.loads(body)
    token = bodyDict['token']

    exist = Device.objects.filter(token=token, active=True)

    if( len(exist) > 0):
        return HttpResponseBadRequest(json.dumps({'message':'el token ya existe'}))

    device = Device()
    device.token = token
    device.active = True

    #if request.user.is_authenticated:
    #    device.user=request.user

    try:
        device.save()
        return HttpResponse(json.dumps({'message':'token guardado'}))
    except:
        return HttpResponseBadRequest(json.dumps({'message':'no se ha podido guardar'}))