from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import users
from product.models import product


def addproducts(request):
    return render(request, 'suppliers/addproducts.html')
def sell(request):
    return render(request, 'suppliers/sell.html')
def selldashboard(request):
        counts = product.objects.count()
        cont= users.objects.count()

        context={

            "countall":counts, 
            "user_count": cont
        }
       
        return render(request, 'suppliers/selldashboard.html',context)
def tables(request):
    user = users.objects.all()
    context = {
        'usersall':user
    }
    return render(request, 'suppliers/tables.html',context)
def billing(request):
    return render(request, 'suppliers/billing.html')
def notifications(request):
    return render(request, 'suppliers/notifications.html')
def sellindex(request):
    return render(request, 'suppliers/sellindex.html')
def profile(request):
    products = product .objects.all()
    context = {
        'productsall':products
    }
    return render(request, 'suppliers/profile.html',context)


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
        
        return Response({"status": "success"})
class ViewUser(TemplateView):
    template_name = 'suppliers/view_user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userdata = users.objects.all()
        context = {"userdata": userdata}
        return context    

class delete_uses(APIView):
    def post(self, request):
        product_name = request.POST["product_name"]
        product.objects.filter(product_name = product_name).delete()
        return JsonResponse({"status":"pass"})
class delete_user(APIView):
    def post(self, request):
        user_name = request.POST["user_name"]
        users.objects.filter(user_name = user_name).delete()
        return JsonResponse({"status":"pass"})
    
class update_staff(APIView):
    def post(self, request):
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        phoneno = request.POST['phoneno']
        role = request.POST['role']
        users.objects.filter(user_name=user_name).update(user_name=user_name, password = password, phoneno =phoneno, role =role)
       
        return Response({"status": "success"})
