from django.shortcuts import render
from faker import Factory
from django.http import JsonResponse
from django.conf import settings

from twilio.rest import Client
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import (
    SyncGrant,
    ChatGrant
)

from .models import Room

def all_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'twilio/index.html', {'rooms': rooms})

def room_detail(request, slug):
    room = Room.objects.get(slug=slug)
    return render(request, 'twilio/chat.html', {'room': room})

def token(request):
    fake = Factory.create()
    device_id = request.GET.get('device', 'default')
    return generateToken(fake.user_name(), device_id)

def generateToken(identity, device_id):
    # Get credentials from environment variables
    account_sid      = settings.TWILIO_ACCT_SID
    chat_service_sid = settings.TWILIO_CHAT_SID
    sync_service_sid = settings.TWILIO_SYNC_SID
    api_sid          = settings.TWILIO_API_SID
    api_secret       = settings.TWILIO_API_SECRET

    # Create access token with credentials
    token = AccessToken(account_sid, api_sid, api_secret, identity=identity)
    endpoint = "MiniSlackChat:{0}:{1}".format(identity, device_id)

    # Create a Sync grant and add to token
    if sync_service_sid:
        sync_grant = SyncGrant(endpoint_id=endpoint, service_sid=sync_service_sid)
        token.add_grant(sync_grant)

    # Create a Chat grant and add to token
    if chat_service_sid:
        chat_grant = ChatGrant(endpoint_id=endpoint, service_sid=chat_service_sid)
        token.add_grant(chat_grant)

    # Return token info as JSON
    return JsonResponse({'identity':identity,'token':token.to_jwt().decode('utf-8')})