from django.shortcuts import render

# Create your views here.
def trial_function(request):
    return render(request, 'trial_view.html', {})
