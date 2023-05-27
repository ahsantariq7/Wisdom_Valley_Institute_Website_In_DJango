from email.message import EmailMessage
from unicodedata import name
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.models import User
from .models import Contact
from datetime import date, datetime
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse  
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

 

# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'commons/signup.html'


# Edit Profile View
class ProfileView(UpdateView):
    model = get_user_model
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'commons/profile.html'
    #User=get_user_model
    #return render(request, 'commons/profile.html', {"form":User})


def contact(request):
    if request.method == 'POST':
        
        name=request.POST['name']
        email=request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        contact=Contact(name=name, email=email, phone=phone, desc=desc,date=datetime.today())
        contact.save()

        #sendEmail
        email_send=EmailMessage(
            'Wisdom Valley Official',#subject
            f'Hi There!Mr/Ms.{name}\n, Thanks for contacting us.\nThis is Your {phone} \n and your message is:\n\n\n {desc}\n\n Thanks For Contacting Us',
            settings.EMAIL_HOST_USER,
            [email]
        )

        email_send.fail_silently=True
        email_send.send()



        messages.success(request, 'A Contact Message Received.')
    #return HttpResponse("This is Service page")
    #return HttpResponse("This is Contact page")
    return render(request, 'contact.html',{})     

def course_detail(request,slug):
    '''
    products=Product.objects.filter(slug=slug)
    if products.exists():
        products=Product.objects.filter(slug=slug)
    else:
        return redirect('404')


    context={
        'products':products,
    }

    return render(request, 'product_detail.html',context)


'''