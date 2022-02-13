from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from personal_blog.contact.forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f"Message from {form.cleaned_data['name']}"
            body = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "company": form.cleaned_data["company"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, form.cleaned_data["email"], ['mkokonyan@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("success message")

    form = ContactForm()
    context = {
        "form": form,
    }

    return render(request, "contact/contact.html", context)


def success_view(request):
    return render(request, "contact/success_message.html")
