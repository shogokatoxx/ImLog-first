from django.shortcuts import render,get_object_or_404,redirect
from .models import Log
from django.contrib.auth.models import User
from .forms import PostForm

def top_page(request):
    return render(request,'logapp/top.html',{})

def lists(request):
    logs = Log.objects.all()
    ranking = Log.objects.all().order_by('votes').reverse()
    newtitle = Log.objects.all().order_by('created_date').reverse()
    return render(request,'logapp/lists.html',{'logs':logs,'ranking':ranking,'newtitle':newtitle})

def log_detail(request,pk):
    logs = get_object_or_404(Log,pk=pk)
    return render(request,'logapp/detail.html',{'logs':logs})

def user_detail(request,pk):
    logs = get_object_or_404(Log,pk=pk)
    return render(request,'logapp/user_detail.html',{'logs':logs})

def user_title(request):
    me = request.user
    logs = Log.objects.filter(user=me)
    return render(request,'logapp/user_title.html',{'logs':logs})

def new_title(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            logs = form.save(commit=False)
            logs.user = request.user
            logs.save()
            return redirect('logapp:lists')
    else:
        form = PostForm()
    return render(request,'logapp/new_title.html',{'form':form})


def edit_title(request,pk):
    log = get_object_or_404(Log,pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=log)
        if form.is_valid():
            logs = form.save(commit=False)
            logs.user = request.user
            logs.save()
            return redirect('logapp:lists')
    else:
        form = PostForm(instance=log)
    return render(request,'logapp/edit_title.html',{'form':form})

def delete(request,pk):
    logs = get_object_or_404(Log,pk=pk)
    logs.delete()
    return redirect('logapp:lists')

def good(request,pk):
    logs = get_object_or_404(Log,pk=pk)
    logs.votes += 1
    logs.save()
    return redirect('logapp:log_detail',pk=logs.pk)
