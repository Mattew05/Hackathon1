from django.shortcuts import render

# Create your views here.

def frontpage(request):
    return render(request, 'Info/frontpage.html')
def descriere(request):
    return render(request, 'Info/descriere.html')
def inceput(request):
    return render(request, 'Info/inceput.html')
def teren(request):
    return render(request, 'Info/teren.html')
def plante(request):
    return render(request, 'Info/plante.html')
def animale(request):
    return render(request, 'Info/animale.html')
def tech(request):
    return render(request, 'Info/tech.html')