import json

from django.shortcuts import render
from faker import Factory
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt

from twilio.rest import Client
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import (VideoGrant, ChatGrant)
from twilio.base.exceptions import TwilioRestException

# Get credentials from environment variables
account_sid = settings.TWILIO_ACCT_SID
chat_service_sid = settings.TWILIO_CHAT_SID
sync_service_sid = settings.TWILIO_SYNC_SID
api_sid = settings.TWILIO_API_SID
api_secret = settings.TWILIO_API_SECRET

twilio_client = Client(api_sid, api_secret, account_sid)


# Create your views here.
def landing(request):
    return render(request, 'twilio/video.html')


@csrf_exempt
def token(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        username = body['username']
        conversation = get_chatroom('My Room')

        try:
            conversation.participants.create(identity=username)
        except TwilioRestException as exc:
            # do not error if the user is already in the conversation
            if exc.status != 409:
                raise

        token = AccessToken(account_sid,
                            api_sid,
                            api_secret,
                            identity=username)
        token.add_grant(VideoGrant(room='My Room'))
        token.add_grant(ChatGrant(service_sid=conversation.chat_service_sid))

        return JsonResponse({'token': token.to_jwt().decode('utf-8')})


def get_chatroom(name):
    for conversation in twilio_client.conversations.conversations.list():
        if conversation.friendly_name == name:
            return conversation

    # a conversation with the given name does not exist ==> create a new one
    return twilio_client.conversations.conversations.create(friendly_name=name)
