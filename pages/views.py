from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def index(request):
  
  return render(request, 'pages/index.html')


def example_endpoint(request):
    return JsonResponse({"message": "Hello from HTMX!"})
  
  




def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')
  
from django.core.mail import send_mail
from django.shortcuts import render, redirect

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email_or_phone = request.POST.get("email_or_phone")
        message = request.POST.get("message")

        full_message = f"From: {name}\nContact: {email_or_phone}\n\n{message}"

        send_mail(
            "New Contact Form Submission",
            full_message,
            "noreply@applikasi.tech",  # Must match your verified sender domain
            "roslan@applikasi.tech",  # Replace with the recipient's email
            fail_silently=False,
        )

        return redirect("success_page")  # Change to your success page

    return render(request, "contact.html")
