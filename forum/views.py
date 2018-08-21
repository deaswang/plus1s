
from datetime import datetime, timedelta
from django.shortcuts import render, get_object_or_404

from .models import Thread, Post, Comment

def index(request):
    thread_list = Thread.objects.order_by('-life')
    context = {
        'thread_list': thread_list,
    }
    return render(request, 'index.html', context)


def thread(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    if request.method == 'POST':
        name = request.POST['name']
        content = request.POST['content']
        add = Post(thread=thread, pub_name=name, pub_date=datetime.now(), content=content)
        add.save()
    try:
        post_list = Post.objects.filter(thread=thread).order_by('pub_date')
    except:
        post_list = None
    return render(request, 'thread.html', {'thread': thread, "post_list": post_list})


def newthread(request):
    if request.method == 'POST':
        title = request.POST['title']
        name = request.POST['name']
        content = request.POST['content']
        add = Thread(title=title, pub_name=name, pub_date=datetime.now(), content=content,
                     life=timedelta(days=1))
        add.save()
        thread_list = Thread.objects.order_by('-life')[:10]
        context = {
            'thread_list': thread_list,
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'newthread.html', {})

