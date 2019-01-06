from django.shortcuts import render

# Create your views here.
def index(request):
    template = "home/index.html"
    context = {}
    return render(request, template, context=context)
def about(request):
    template = "home/about.html"
    context = {}
    return render(request, template, context=context)
