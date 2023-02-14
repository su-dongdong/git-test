from django.shortcuts import render
from django.http import HttpRequest, JsonResponse


# Create your views here.

def test_git(request: HttpRequest):
    print('git test')
    return JsonResponse({"code": 200})
