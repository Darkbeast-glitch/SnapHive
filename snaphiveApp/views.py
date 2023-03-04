from django.shortcuts import render
from .models import Contact, newsLetter
from django.contrib import messages


# Create your views here.


def HomePage(request):

    contact = Contact.objects.all()
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        category = request.POST["category"]
        others = request.POST["otherInput"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        contact_form = Contact(fullname=name, email=email, phone=phone, category=category, others=others,
                               subject=subject, message=message)
        contact_form.save()

        messages.success(
            request, "Your message has been received, SnapHive rep will get to you in less than 24hrs.")
        contact_form.save()

        # # letteremail = newsLetter.objects.all()
        # if request.method == 'POST':
        #     email_letter = request.POST['newsletter_email']

        #     email_form = newsLetter(email=email_letter)
        #     email_form.save()

        #     messages.success(
        #         request, "Your message has been received, SnapHive rep will get to you in less than 24hrs.")
        # contact_form.save()

    context = {
        'contact': contact,

    }

    return render(request, 'index.html', context)
