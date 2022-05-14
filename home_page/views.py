from django.shortcuts import render

context3 = {
    "home_wel": "Its HOOOOOOOOME",
}


def home(request):
    return render(request, 'home.html', context3)
