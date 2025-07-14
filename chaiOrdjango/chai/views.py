from django.shortcuts import render

# Create your views here.

def chai_view(request):
    return render(request, 'chai.html')