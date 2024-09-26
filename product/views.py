from django.shortcuts import render
from product.models import product
from order.models import cart
from suppliers.models import vendor
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.http import HttpResponse






def landing(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "product/landing.html")
def products(request):
    products = product .objects.all()
    context = {
        'productsall':products
    }
    return render(request,"product/products.html",context)
def cart(request):
    return render(request, 'product/cart.html')
def signup(request):
    return render(request,"product/signup.html")
def adminn(request):
    return render(request,"product/admin.html")
def addproducts(request):
    return render(request, "suppliers/addproducts.html")
def sell(request):
    return render(request, "suppliers/sell.html")
def cartnew(request):
    return render(request, "product/cartnew.html")

# Create your views here.
class Createproducts(APIView):
    def post(self, request):
        product_name = request.POST['product_name']
        price = request.POST['price']
        quantity = request.POST['quantity']
        add_image = request.POST['add_image']
        
        # Create a new user
        user = product()
        user.product_name = product_name
        user.price = price
        user.quantity = quantity
        user.add_image = add_image
        
        # Save the user instance to the database
        user.save()
        
        return Response({"status": "success"}, status=status.HTTP_201_CREATED)
    
class Createcart(APIView):
    def post(self, request):
        cname = request.POST['cname']
        cemail = request.POST['cemail']
        caddress = request.POST['caddress']
        cphoneno = request.POST['cphoneno']
        
        # Create a new user
        cart = cart()
        cart.name = cname
        cart.email = cemail
        cart.address = caddress
        cart.phoneno = cphoneno
        # Save the user instance to the database
        cart.save()
        
        return Response({"status": "success"}, status=status.HTTP_201_CREATED)
    

class CreateSell(APIView):
    def post(self, request):
        name = request.POST['sname']
        email = request.POST['semail']
        password = request.POST['spassword']
        phoneno = request.POST['sphoneno']
        
        # Create a new user
        user = vendor()
        user.name = name
        user.email = email
        user.password = password
        user.phoneno = phoneno
        
        # Save the user instance to the database
        user.save()
        return Response({"status": "success"}, status=status.HTTP_201_CREATED)
    from django.shortcuts import render


def check_user(request):
    # Example: Get username from request, e.g., a form submission
    name = request.GET.get('name', '')

    if vendor.objects.filter(name=name).exists():
        return HttpResponse("User is present.")
    else:
        return HttpResponse("User is not present.")
