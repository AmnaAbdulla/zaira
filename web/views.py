from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, ContactForm ,CheckOutForm
from django.http import HttpResponse, JsonResponse
from . models import Featured,Ethnic,Western,Party,Paksthani,Prayer
import json
from django.shortcuts import render, get_object_or_404
from .models import Product  



# Create your views here.
def index(request):
    category=Featured.objects.filter()
    return render(request,'index.html',{'category':category})

def indus(request):
    return render(request,'product.html')

def ethnic(request):
    return render(request,'product.html')

def ethnicwear(request):
     categoryethinic=Ethnic.objects.filter()
     return render(request,'ethnic.html',{'categoryethinic':categoryethinic})

def western(request):
     categorywestern=Western.objects.filter()
     return render(request,'western.html',{'categorywestern':categorywestern})

def party(request):
     categoryparty=Party.objects.filter()
     return render(request,'partywear.html',{'categoryparty':categoryparty})

def paksthani(request):
     categorypaksthani=Paksthani.objects.filter()
     return render(request,'paksthani.html',{'categorypaksthani':categorypaksthani})

def prayer(request):
     categoryprayer=Prayer.objects.filter()
     return render(request,'prayer.html',{'categoryprayer':categoryprayer})

def quick_view(request, product_id):
    item = get_object_or_404(Product, id=product_id)
    return render(request, 'quick_view.html', {'item': item})

def signup(request):
	if request.method =='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request,user)
			# messages.success(request, ('Youre now registered'))
			return redirect('signin')
	else: 
		form = SignUpForm() 

	context = {'form': form}
	return render(request,'signup.html', context)
          
def signin(request):
	if request.method == 'POST': #if someone fills out form , Post it 
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:# if user exist
			login(request, user)
			# messages.success(request,('Youre logged in'))
			return redirect('templates:index') #routes to 'home' on successful login  
		else:
			# messages.success(request,('Error logging in'))
			return redirect('login') #re routes to login page upon unsucessful login
	else:
    		return render(request,"signin.html")

# def logout_1(request):
#     logout(request)
#     return redirect('web:index')

def logout_user(request):
	logout(request)
	# messages.success(request,('Youre now logged out'))
	return redirect('signin')

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST, request.FILES)8
#         if form.is_valid():
#             form.save()
#     else:
#         form = ContactForm()
#     return render(request, 'web/contact.html', {'form': form})

def contact(request):
    # Create an instance of the ContactForm, either with POST data or None
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        # If the request method is POST, check if the form data is valid
        if form.is_valid():
            # If the form data is valid, save it to the database
            form.save()
            # Create a JSON response indicating success
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            # If the form data is not valid, create a JSON response indicating failure
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
                "message": "Please correct the errors below and try again.",
            }
        
        # Return a JSON response with the appropriate message
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        # If the request method is not POST, render the contact form template with the ContactForm instance
        context = {
            "is_contact": True,
            "form": form,
        }
        return render(request, "contact.html", context)
    
def category(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    product = Product.objects.all()

    if min_price and max_price:
        product = product.filter(price__range=(min_price, max_price))

    context = {
        'product': product,
        'min_price': min_price,
        'max_price': max_price,
        
    }

    return render(request, 'category.html', context)


def checkout(request):
    product_id = request.GET.get("product_id")
    cart = request.session.get("cart", {})
    product = cart.get(str(product_id), {})  # Get the product from session

    if request.method == "POST":
        form = CheckOutForm(request.POST)
        if form.is_valid():
            form.save()
            # Instead of redirecting, just reload the same page with a success message
            messages.success(request, "Your order has been submitted successfully.")
            form = CheckOutForm()  # Reset the form after successful submission
    else:
        form = CheckOutForm()

    context = {
        "is_checkout": True,
        "product_id": product_id,
        "product": product,
        "form": form
    }
    return render(request, "checkout.html", context)



def cart(request):
    context = {"is_cart": True}
    return render(request, "cart.html", context)



# @login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("category")


def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")



def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")



def cart_detail(request):
    return render(request, 'cart.html')

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")