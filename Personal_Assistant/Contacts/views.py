from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Contact
from .forms import ContactForm, ContactSearchForm, DaysAheadForm

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='contacts:contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(to='contacts:contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_form.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect(to='contacts:contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})


def contact_search(request):
    form = ContactSearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = ContactSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Contact.objects.filter(name__icontains=query)
    return render(request, 'contacts/contact_search.html', {'form': form, 'query': query, 'results': results})

def upcoming_birthdays(request):
    form = DaysAheadForm(request.GET or None)
    upcoming_birthdays = []
    days_ahead = 7  # Default value
    
    if form.is_valid():
        days_ahead = form.cleaned_data['days_ahead']
        # Check if the number of days is within a reasonable range
        if 1 <= days_ahead <= 365:
            today = timezone.now().date()
            start_date = today
            end_date = today + timedelta(days=days_ahead)
   
            upcoming_birthdays = Contact.objects.filter(
                birthday__month__gte=start_date.month,
                birthday__day__gte=start_date.day,
                birthday__month__lte=end_date.month,
                birthday__day__lte=end_date.day
)
             
  
        else:
            # If the number of days is out of range, clear the form and show an error message
            form = DaysAheadForm()
            days_ahead = 7

    
    return render(request, 'contacts/upcoming_birthdays.html', {
        'form': form,
        'upcoming_birthdays': upcoming_birthdays,
        'days_ahead': days_ahead
    })  