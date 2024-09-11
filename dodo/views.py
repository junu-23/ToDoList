from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import Doit
from django.utils import timezone
from django.urls import reverse

def index(request):
    doit_list =  Doit.objects.filter(is_done=False).order_by('-create_date')
    #  doit_list = Doit.objects.all().order_by('-create_date')
    return render(request, 'dodo/index.html', {'doit_list': doit_list})
    #  context는 뷰에서 템플릿으로 데이터 전달함

def doit_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            doit = form.save(commit=False)
            doit.create_date = timezone.now()
            doit.save()
            return redirect('dodo:index')
    else:
        form = TodoForm()
    return render(request, 'dodo/doit_form.html', {'form': form})

def DoitDetail(request, pk):
    doit = get_object_or_404(Doit, pk=pk)
    return render(request, 'dodo/doit_detail.html', {'doit': doit})

def doit_delete(request, pk):
    doit = get_object_or_404(Doit, pk=pk)
    doit.delete()
    return redirect('dodo:index')
    #  여기서의 dodo도 네임스페이스(app_name)

def doit_modify(request, pk):
    doit = get_object_or_404(Doit, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=doit)
        if form.is_valid():
            form.save()
            return redirect('dodo:index')
    else:
        form = TodoForm(instance=doit)
        context = {'form': form}
        return render(request, 'dodo/doit_form.html', context)

def done_list(request): #  완료된 할일들 표시
    done_tasks = Doit.objects.filter(is_done=True).order_by('-create_date')
    return render(request, 'dodo/done_list.html', {'done_tasks': done_tasks})

def doit_done(request, pk):
    #  request 객체는 항상 view함수에 항상 포함되어야 함
    doit = get_object_or_404(Doit, pk=pk)
    doit.is_done = True
    doit.save()
    return redirect('dodo:index')

def done_delete(request, pk):
    doit = get_object_or_404(Doit, pk=pk)
    doit.delete()
    return redirect('dodo:done_list')





