from django.utils import timezone
from django.shortcuts import render
from .models import Note
from datetime import datetime


today = datetime.now()

def home(request):
    
    current_notes = []
    if request.user.is_authenticated:
        current_notes = Note.objects.filter(dateStart__lte=today, dateEnd__gte=today, author=request.user.pk)   
    
    data = {
        'current_notes': current_notes,
    }
    
    return render(request, "main/index.html", context=data)


def tasks(request):
    
    notes = []
    if request.user.is_authenticated:
        notes = Note.objects.filter(author=request.user.pk)
    
    data = {
        'notes':notes,
    }
    
    return render(request, 'main/tasks.html', context=data)


def task(request, note_pk):
    
    note = Note.objects.get(pk=note_pk)
    
    data = {
        'note': note,
    }
    
    return render(request, 'main/task.html', context=data)