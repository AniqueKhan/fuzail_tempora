from django.shortcuts import render
from fuzail_app.forms import ContactForm
from fuzail_app.models import Contact
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
def index(request):
    form = ContactForm
    context = {
        "form":form
    }
    return render(request,"index.html",context)


def contact_view(request):
    if request.method == "POST" and request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            message = form.cleaned_data.get("message")
            subject = form.cleaned_data.get("subject")


            Contact.objects.create(email=email,subject=subject, first_name=first_name,last_name=last_name, message=message)



            return JsonResponse({"success": True})
        else:
            return JsonResponse({"errors": form.errors}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)