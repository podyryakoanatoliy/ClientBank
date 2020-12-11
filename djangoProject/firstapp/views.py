from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


def index(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            birthday = request.POST.get("birthday")
            card = request.POST.get("card")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            data={"Name": name, "Surname": surname, "Birthday": birthday, "Card": card, "Phone": phone, "Email": email}
            return render(request, "information.html", context=data)
        else:
            return HttpResponse("Invalid data")
    else:
        userform = UserForm()

        return render(request, "index.html", {"form": userform})