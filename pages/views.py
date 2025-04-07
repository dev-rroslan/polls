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


from django.core.mail import send_mail
from django.shortcuts import render, redirect

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email_or_phone = request.POST.get("contact")
        message = request.POST.get("message")

        full_message = f"From: {name}\nContact: {email_or_phone}\n\n{message}"

        send_mail(
            "New Contact Form Submission",
            full_message,
            "noreply@applikasi.tech",  # Sender email address
            ["dev.rroslan@gmail.com"],  # Recipient email address as a list
            fail_silently=False,
        )

        return redirect("success_page")  # Redirect to a success page after submission

    return render(request, "pages/contact.html")  # Render the contact form page


def success_page(request):
    return render(request, 'pages/success.html')

