from django.urls import re_path
from helloworld.views import first_view_func


urlpatterns = [
     # 进行url地址配置: 把浏览器访问url地址和对应视图关联起来
     # re_path("url地址: 正则表达式","view 试图")
    re_path(r'^hello-world/$', first_view_func)
]