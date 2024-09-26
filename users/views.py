

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic.base import TemplateView
from .models import users  # Ensure correct import path

# Define your other views here
def landing(request):
    return render(request, 'product/landing.html')

def products(request):
    return render(request, 'ecopro/products.html')

def signup(request):
    return render(request, 'ecopro/signup.html')



def dashboard(request):
    return render(request, 'product/dashboard.html')


class delete_user(APIView):
    def post(self, request):
        emails = request.POST["email"]
        users.objects.filter(email = emails).delete()
        return JsonResponse({"status":"pass"})

class CreateStaff(APIView):
    def post(self, request):
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        phoneno = request.POST['phoneno']
        role = request.POST['role']
        
        # Create a new user
        user = users()
        user.user_name = user_name
        user.email = email
        user.password = password
        user.phoneno = phoneno
        user.role = role
        
        # Save the user instance to the database
        user.save()
        
        return Response({"status": "success"}, status=status.HTTP_201_CREATED)

class update_staff(APIView):
    def post(self, request):
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        phoneno = request.POST['phoneno']
        role = request.POST['role']
        users.objects.filter(user_name=user_name).update(user_name=user_name, password = password, phoneno =phoneno, role =role)
       
        return Response({"status": "success"})

class login_check(APIView):
    def post(self, request):
        
        email = request.data.get("email")
        password = request.data.get("password")
        print("email:", email)
        print("password:", password)
        user=users.objects.filter(email=email,password=password).values()
        print("*******:",user)
        
        if (len(user) > 0):
            return JsonResponse({"status": "pass", "users": user[0]["email"],"role": user[0]["role"]})
        else:
           return JsonResponse({"status": "fail"}) 
        
        
       
        
# Define other class-based views here

class ViewUser(TemplateView):
    template_name = 'product/view_user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userdata = users.objects.all()
        context = {"userdata": userdata}
        return context
    
    
