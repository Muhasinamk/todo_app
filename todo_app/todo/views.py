from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .forms import LoginForm, RegisterForm
from .models import Tasks, Login


# Create your views here.

def register_fun(request):
   login=Login.objects.all()
   form=RegisterForm()

   if request.method=='POST':
       form=RegisterForm(request.POST)
       if form.is_valid():
           form.save()
       return redirect('/login/')
   context={'register':login,'form':form}
   return render (request,"register.html",context)

def login_fun(request):
    context={}
    form=LoginForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/task-list')
    context['form']  =form
    return render(request,"login.html",context)


class TaskList(ListView):
    model=Tasks
    context_object_name = 'task'
    template_name = 'tasklist.html'

class TaskCreate(CreateView):
    model=Tasks
    fields='__all__'
    success_url=reverse_lazy('task')
    template_name='taskcreate.html'

class TaskUpdate(UpdateView):
    model=Tasks
    fields='__all__'
    success_url=reverse_lazy('task')
    template_name='taskcreate.html'

class TaskDelete(DeleteView):
    model=Tasks
    field='__all__'
    success_url=reverse_lazy('task')
    template_name='taskdelete.html'


class TaskDetailView(DetailView):
    model=Tasks
    template_name = 'taskdetail.html'
