from django.shortcuts import render

context2 = {
    "dam": "daaaaaaaaaam",
}


def contacts(request):
    return render(request, '1c.html', context2)
