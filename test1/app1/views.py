from django.shortcuts import render
from django.http import HttpRequest, JsonResponse


# Create your views here.

def test_git(request: HttpRequest):
    print('git test')
    print('世界那么大，我想去看看')
    return JsonResponse({"code": 200})
