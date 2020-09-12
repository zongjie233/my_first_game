from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#视图是接收httprequest对象并返回一个httpresponse对象的Python函数。接收 request 作为参数并返回 response 作为结果。
def home(request):
    return HttpResponse('my first web!!!!!')


