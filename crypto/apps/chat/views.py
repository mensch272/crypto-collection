from django.shortcuts import render


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    context = {
        'room_info': {
            'room_name': room_name,
            'alias': request.GET.get('alias', 'Anonymous'),
        }
    }

    return render(request, 'chat/room.html', context)
