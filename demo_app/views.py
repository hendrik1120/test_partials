from django.shortcuts import render

from demo_app.models import TestModel


def partial_view(request):
    template = "base.html#test_partial"
    context = {"test": TestModel.objects.all()}
    return render(request, template, context)

def regular_view(request):
    template = "base.html"
    context = {"test": TestModel.objects.all()}
    return render(request, template, context)