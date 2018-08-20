from django.shortcuts import render, get_object_or_404

from .models import Thread, Post, Comment

def index(request):
    thread_list = Thread.objects.order_by('-life')[:10]
    context = {
        'thread_list': thread_list,
    }
    return render(request, 'index.html', context)


def thread(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    return render(request, 'thread.html', {'thread': thread})


