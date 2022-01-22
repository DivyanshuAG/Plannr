from django.shortcuts import render

def create_event(request):
    # POST handler to create a new event
    # TODO: make the 'day' parameter automatically syncronize based on start_time and end_time
    return

def update_event(request):
    # POST handler to update event
    # TODO: same as above
    return

def remove_event(request):
    # easy shorthand to remove request of specific <int:pk>
    return

def sycnronize_day_and_time(start_time, end_time):
    # helper function to syncronize the start_time, end_time and days affected.
    return

