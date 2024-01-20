from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Tasks
from .serializers import TasksSerializer
from django import forms
from rest_framework import viewsets

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

"""class AddTaskForm(forms.Form):
    name = forms.CharField(
        label="Task Name",
        widget=forms.TextInput(attrs={'style': 'width: 500px;', 'autofocus': True})
    )
    description = forms.CharField(
        label="Task Description",
        widget=forms.Textarea(attrs={'rows': 6, 'cols': 100, 'placeholder':'Add Description...'})
    )"""

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'style': 'width: 500px;', 'autofocus': True}),
            'description': forms.Textarea(attrs={'rows': 6, 'cols': 100, 'placeholder': 'Add Description...'}),
        }

# Create your views here.
def index(request):

    tasks = Tasks.objects.all()

    if request.method == "POST":
        selected_ids = request.POST.getlist("mark")
        selected_tasks = tasks.filter(pk__in=selected_ids)
        for t in selected_tasks:
            t.completed = True
            t.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        sorted_tasks = tasks.order_by('-id').values()
        return render(request, "tasks/index.html", {
            "tasks":sorted_tasks
        })
    

def add(request):
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            new_task = Tasks(name=name, description=description)
            new_task.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    else:
        return render(request, "tasks/add.html", {
            "form": AddTaskForm()
        })
