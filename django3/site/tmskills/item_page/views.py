from django.shortcuts import render
from django.shortcuts import redirect

def catalog_page(request):
    if request.method == "POST":
        print(request.POST)
        redirect("/catalog/")
    return render(request, template_name="catalog.html", context={})