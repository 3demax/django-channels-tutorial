import json
from django.shortcuts import render
from django.utils.safestring import mark_safe

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def index(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('chat_lobby', {
        'type': 'chat_message',
        'message': 'someone loaded index'
    })
    async_to_sync(channel_layer.send)('task1', {
        'type': 'test.print',
        'message': 'someone loaded index'
    })
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })