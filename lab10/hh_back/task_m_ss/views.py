from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the task_m_s index.")


def hello(request):
    return HttpResponse("Hello from Olzhas!")

