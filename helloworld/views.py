from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# 在子应用下面得views.py文件中定义 view试图
# view 视图其实就是一个函数, 这个函数得作用是接收客户端得请求,并且处理之后返回响应


def first_view_func(request):
    """
    request :请求对象 包含客户端得请求时传递报文得数据
    根据客户端得请求 进行具体得操作
    返回响应
    """
    return HttpResponse("<h1>hello world</h1>")