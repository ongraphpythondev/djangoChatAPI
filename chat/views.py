from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from .openapi import chatResponse
from .models import Chat,User, Book
import json
from .serializers import SnippetSerializer
from django.contrib.auth import authenticate
# Create your views here.

@method_decorator(csrf_exempt, name="dispatch")
class Signup(View):
    def get(self,request):
        return render(request, "signup.html")

    def post(self, request):
        data = request.POST
        print(data) 

        user = User.objects.filter(email=data['email']).first()
        if user:
            return JsonResponse({"msg":"Already exist!"},status=404)
        print(data['password'],data['confirm_password'])
        if data['password']!=data['confirm_password']:
            return JsonResponse({"msg":"Password not match!"},status=404)
        print(data)
       
        User.objects.create_user(username=data['name'],email=data['email'],password=data['password'],mobile=data['mobile'])
        
        return JsonResponse({"msg":"User Creted"},status=200)

@method_decorator(csrf_exempt, name="dispatch")
class Home(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self,request):
        data = request.POST.get("text")
        print(data)
        res = chatResponse(data)
        Chat.objects.create()
        return JsonResponse({"msg":res})

@method_decorator(csrf_exempt, name="dispatch")
class LoginView(View):
    def get(self,request):
        return render(request,"login.html")
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        # user = load_user(username)
        # print(username,password,user)
        error = []
        if user is not None:
            return redirect('/')

        error.append("Invalid credentials!")
        return render(request,"login.html",context={"request":request, "error":error})

  