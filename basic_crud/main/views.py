from django.shortcuts import render
from ninja import NinjaAPI

# Create your views here.
api = NinjaAPI()


@api.get("/hello")
def hello(request):
    return {"Hello World": "First Main Attempt"}
