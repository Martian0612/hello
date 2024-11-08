from django.shortcuts import render , HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # context is a set of variable jo aap bhejte ho apne template main (basically it's a dictionary.)
    context = {
        "variable1" : "I am your variable ele!",
        "variable2" : "I am your second variable element!"
    }
    # return render(request,'index.html',context) // for returning the variable to template from index function.
    return render(request,'index.html')
    # return HttpResponse('This is Martian, just testing!')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is Martian about page!")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name = name, email = email, phone = phone, desc = desc)
        messages.success(request,"Form submitted successfully!")
        contact.save()

    return render(request, 'contact.html')
    # return HttpResponse("Contact me at blackabyss2709@gmail.com or at number 7389560834")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("We provide photography services.")

def examples(request):
    return render(request, 'examples.html')