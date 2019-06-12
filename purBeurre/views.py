from django.shortcuts import render


# Create your views here.


def accueil_view(request):
    utilisateur = request.user
    return render(request, 'accueil_view.html', {})
