from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return HttpResponse("Hello, World!")

def form_view(request):
    return render(request,'form.html')


    
def calculate(request):
    if request.method == 'POST':
        num1 = int(request.POST['num1'])
        num2 = int(request.POST['num2'])
        operation = request.POST.get('operation')
        
        if operation == 'add':
            result = num1+num2
            message=f'the sum of {num1} and {num2} is {result}'
        elif operation == 'subtract':
            result = num1-num2
            message = f'the difference of {num1} and {num2} is {result}'
        elif operation == 'divide':
            result = num1/num2
            message = f'the division of {num1} and {num2} is {result}'
        elif operation == 'multiply':
            result = num1*num2
            message = f'the multiplication of {num1} and {num2} is {result}'
        
        else:
            message ='invalid operation'

        return HttpResponse(message)
    else:
        return HttpResponse('invalid request provided')