# from django.shortcuts import render
from django.http import HttpRequest, JsonResponse


# Create your views here.

def test_git(request: HttpRequest):
    print('git test')
    print('世界那么大，我想去看看')
    print('test')
    print("世界那么大， 我想去看看")
    print("master test")
    print("hot-fix")
    print("test2")
    print("pull test")
    print("gitee test")
    return JsonResponse({"code": 200})
