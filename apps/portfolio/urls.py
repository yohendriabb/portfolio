from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PortfolioView

router = DefaultRouter()

router.register('portfolio', PortfolioView, basename="portfolio")


urlspatterns = [
	path('', include(router.urls))
]