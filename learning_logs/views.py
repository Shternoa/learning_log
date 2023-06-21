from django.shortcuts import render
from .models import Topic
from .forms import TopicForm, EntryForm

from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    """Домашняя страница приложения Learning Log"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Список тем"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Выводит одну тему и все ее записи."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Определение новой темы"""
    if request.method != 'POST':
        # Данные не отправились и создается пустая форма
        form = TopicForm()
    else:
        # Отправлены данные POST, обработка данных
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Добовляет новую запись по конкретной теме"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Данные не отправились и созадается новая форма
        form = EntryForm()
    else:
        # Данные отправлены в POST и обрабатываются
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
