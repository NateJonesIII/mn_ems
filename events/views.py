# events/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Event, RSVP
from .forms import EventForm, RSVPForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'events/home.html')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    rsvp, created = RSVP.objects.get_or_create(user=request.user, event=event)
    
    if request.method == 'POST':
        form = RSVPForm(request.POST, instance=rsvp)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=event_id)
    else:
        form = RSVPForm(instance=rsvp)
    
    return render(request, 'events/event_detail.html', {'event': event, 'form': form, 'rsvp': rsvp})

@login_required
def event_rsvp(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    rsvp, created = RSVP.objects.get_or_create(event=event, user=request.user)
    if request.method == 'POST':
        form = RSVPForm(request.POST, instance=rsvp)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = RSVPForm(instance=rsvp)
    return render(request, 'events/event_detail.html', {
        'event': event,
        'form': form,
        'rsvp': rsvp if rsvp.status else None
    })

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user  # Assign the logged-in user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})

def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})

def faq_view(request):
    # Define logic for FAQ page here
    return render(request, 'faq.html')  # Replace with your FAQ template name