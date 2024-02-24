from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return HttpResponse("Hello, World!")

def form_view(request):
    return render(request,'form.html')

def calculate_add(request):
    if request.method == 'POST':
        num1 = int(request.POST['num1'])
        num2 = int(request.POST['num2'])
        result=num1 + num2
        return HttpResponse(f'the sum of {num1} and {num2} is {result}')
    else:
        return HttpResponse('invalid calculation request')