from django.shortcuts import render, redirect

from .forms import TopicForm, EntryForm

from .models import Topic

# Create your views here.
def index(request):
    #get requesting from database
    #post post information to the database
    return render(request, 'MainApp/index.html')

def topics(request):
    topics = Topic.objects.order_by('-date_added')
    #'-' before date_added is for descending order since ascending is the normal

    context = {'topics':topics}
    #key is variable used in template file html file, value of the dictionary is the variable used in the view function

    return render(request, 'MainApp/topics.html')

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    entries = topic.entry_set.all()

    context = {'topic':topic, 'entries':entries}
    #key represents variabel name to use in template and value represents variable name used in view

    return render(request, 'MainApp/topics.html')

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect('MainApp:topics')

    context = {'form':form}
    return render(request, 'MainApp/new_topic.html', context)
    #what is context: it's a dictionary that allows us to pass data to our template

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()

            return redirect('MainApp:topic',topic_id=topic_id)