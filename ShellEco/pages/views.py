from django.shortcuts import render


def index(request):
    return render(request, 'pages/teamEcoTitans.html')


def about(request):
    return render(request, 'pages/teamEcoTitansAbout.html')


def team(request):
    return render(request, 'pages/teamEcoTitansTeam.html')


def efficiency(request):
    return render(request, 'pages/teamEcoTitansEfficiency.html')


def sponsors(request):
    return render(request, 'pages/teamEcoTitansSponsors.html')




