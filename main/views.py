from winreg import DeleteValue

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import RegisterUserForm
from .models import Task

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


class RegisterView(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name: str = 'main/register.html'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'deadline']
        widgets = {
            'deadline': forms.DateInput()
        }


class CreateObj(CreateView):
    form_class = TaskForm
    model = Task
    success_url = reverse_lazy('main:tasks')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ViewTasks(ListView, LoginRequiredMixin):
    model = Task
    template_name: str = 'main/tasks.html'
    context_object_name = 'task_list'
    success_url = reverse_lazy('main:tasks')

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user).order_by('deadline')


class DeleteTask(DeleteView, LoginRequiredMixin):
    model = Task
    template_name = 'main/delete_task.html'
    success_url = reverse_lazy('main:tasks')


class TaskDetail(DetailView, LoginRequiredMixin):
    model = Task
    template_name = 'main/task.html'


class UpdateTask(UpdateView, LoginRequiredMixin):
    model = Task
    fields = ['name', 'description', 'deadline']
    success_url = reverse_lazy('main:tasks')
