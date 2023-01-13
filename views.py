from django.shortcuts import HttpResponse, redirect
from datetime import datetime

def hello(request):
    if request.method == 'GET':
        return HttpResponse('HELLO ITS MY PROJECT!!!')
def goodbye(request):
    if request.method == 'GET':
        return HttpResponse('GOOD BYE USER!!!')
def date(request):
    cur_date = datetime.now()
    if request.method == 'GET':
        return HttpResponse(cur_date)

