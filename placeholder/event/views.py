from django.shortcuts import render
from .forms import EventForm
from django.views.generic import CreateView, UpdateView
from .models import Event

# def create_event(request):
#     # POST handler to create a new event
#     # TODO: make the 'day' parameter automatically syncronize based on start_time and end_time
#     form = EventForm()
#     if request.method == "POST":
#         form = EventForm(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             print(obj.user)
#             obj.user = request.user
#             print(obj.user)
#             obj.save()
#         return render(request, "event/index.html", {"form": form})
#     else:
#         return render(request, "event/index.html", {"form": form})

class EventCreateView(CreateView):
    model = Event
    fields = ['title', 'description', 'day', 'start_time', 'end_time']
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class Update_event(UpdateView):
    # POST handler to update event
    # TODO: same as above
    model = Event
    fields = ['title', 'description', 'day']

def remove_event(request):
    # easy shorthand to remove request of specific <int:pk>
    return

def sycnronize_day_and_time(start_time, end_time):
    # helper function to syncronize the start_time, end_time and days affected.
    return

