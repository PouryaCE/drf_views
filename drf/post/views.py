from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views import View
from django.views.generic import ListView
from .models import Post
from django.utils import timezone
# Create your views here.


# class PostListView(View):
#     def get(self, request):
#         posts = Post.objects.all().order_by('-created')
#         context = {
#             'posts': posts
#         }
#         return render(request, template_name='post/post_list.html', context=context)




class PostListView(ListView):
    model = Post
    ordering = '-created'
    



class IndexView(View):

    http_method_names = ["get"]

    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
        super().setup(request, *args, **kwargs)
        self.user = request.user
        self.date = timezone.now()
        self.method = request.method

    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        respone = super().dispatch(request, *args, **kwargs)
        if not request.user.is_authenticated:
            return HttpResponse("first you should log in")
        return respone


    def http_method_not_allowed(self, request, *args, **kwargs):
        context = {
            'method':self.method,
            'user': self.user,
            'date':self.date
        }
        return render(request=request, template_name='post/not_allowed.html', context=context)
    

    def head(self, *args, **kwargs):
        print("hello from head ..... ")
        return HttpResponse("hello from head")



    def get(self, request, *args, **kwargs):
        return render(request, 'post/index.html')
    

    def options(self, request: HttpRequest, *args: Any, **kwargs: Any):
        response =  super().options(request, *args, **kwargs)
        response.headers["user"] = self.user
        response.headers["data"] = "some data"