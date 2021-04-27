from django.shortcuts import render
from home.models import Service, Portfolio, PortfolioModal, Team


def homepage(request):
    services = Service.objects.all()
    portfolios = Portfolio.objects.all()
    portfoliomodals = PortfolioModal.objects.all()
    teams = Team.objects.all()
    return render(request, 'index.html', {"services": services, "portfolios": portfolios, "portfoliomodals": portfoliomodals, "teams": teams})
