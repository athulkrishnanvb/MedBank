from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from.forms import BloodRequestForm,BloodDonationForm,SignupForm,BookingForm
from.models import Bloodrequest,BloodDonation,MedicalProduct,Booking
from django.core.files.storage import FileSystemStorage
import uuid
from django.contrib import messages
# Create your views here.


def make_blood_request(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            blood_request = form.save(commit=False)
            blood_request.requester = request.user
            # blood_request.status = 'Pending'
            blood_request.save()
            return redirect(request_succ)
    else:
        form = BloodRequestForm()
    return render(request, 'blood_request.html', {'form': form})

def my_blood_request(request):
    blood_requests = Bloodrequest.objects.filter(requester=request.user)
    return render(request, 'my_bloodrequest.html', {'blood_requests': blood_requests})

def request_succ(request):
    request_code = str(uuid.uuid4()).split('-')[0].upper()
    return render(request, 'request_succ.html',{'request_code':request_code})


def make_blood_donation(request):
    if request.method=='POST':
        form = BloodDonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.donor = request.user
            # donation.status = 'Pending'
            donation.save()
        return redirect(donation_succ)
    else:
        form = BloodDonationForm()
    return render(request, 'blood_donation.html',{'form':form})

def my_blood_donation(request):
    blood_donations = BloodDonation.objects.filter(donor=request.user)
    return render(request, 'my_donations.html',{'blood_donations': blood_donations})

def donation_succ(request):
    donation_code = str(uuid.uuid4()).split('-')[0].upper()
    return render(request, 'donation_succ.html',{'donation_code':donation_code})

def hompg(request):
    return render(request, 'homep2.html')




def homepage(request):
    return render(request, 'homep.html')


def signup(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(login_view)

    else:
        form = SignupForm()
    return render(request, 'signu.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(homepage)
    else:
        form = AuthenticationForm()

    return render(request, 'logi.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect(homepage)



def medadd(request):
    if request.method=='POST':
        myfile=request.FILES['photo']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)

        obj=MedicalProduct()
        obj.photo=filename
        obj.name=request.POST.get('name')
        obj.description=request.POST.get('description')
        obj.quantity=request.POST.get('quantity')
        obj.available=request.POST.get('available')=='on'
        obj.price=request.POST.get('price')
        obj.save()
        return redirect(medi_prods)
    else:
        return render(request, 'med_add.html')
    
def medi_prods(request):
    products = MedicalProduct.objects.all()
    return render(request, 'med_list.html',{'products':products})

def search_p(request):
    query = request.GET.get('query','')
    if query:
        products = MedicalProduct.objects.filter(name__icontains=query)
    else:
        products = MedicalProduct.objects.all()
    return render(request, 'med_list.html',{'products': products})
         

def product_book(request, pk):
    product = get_object_or_404(MedicalProduct, pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.product = product
            booking.user = request.user
            booking.save()
            return redirect('booking_succ')
    else:
        form = BookingForm()
    return render(request, 'booking.html',{'product': product, 'form': form})

def booking_succ(request):
    return render(request, 'book_succ.html')

def profile(request):
    user = request.user
    return render(request, 'profile.html',{'user': user})

def order_view(request):
    orders = Booking.objects.filter(user=request.user)
    return render(request, 'orders.html', {'orders': orders})

def filtered_products(request):
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)

    products = MedicalProduct.objects.all()

    if min_price and min_price.isdigit():
        products = products.filter(price__gte=int(min_price))
    
    if max_price and max_price.isdigit():
        products = products.filter(price__lte=int(max_price))
    
    context = {
        'products': products
    }
    return render(request, 'med_list.html', context)



def cancel_order(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Booking, id=order_id, user=request.user)
        if order.status != 'Canceled': 
            order.status = 'Canceled'
            order.save()
            messages.success(request, 'Order canceled successfully.')
        else:
            messages.warning(request, 'Order is already canceled.')
    else:
        messages.error(request, 'Invalid request method.')
    return redirect('order_view')

def delete_order(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Booking, id=order_id, user=request.user, status='Canceled')
        order.delete()
        messages.success(request, 'Order deleted successfully.')
    else:
        messages.error(request, 'Invalid request method.')
    return redirect('order_view')
