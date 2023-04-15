from django.shortcuts import render


from rest_framework import viewsets


from .models import Portfolio

from .serializers import PortfolioSerializer

class PortfolioView(viewsets.ModelViewSet):
	serializer_class = PortfolioSerializer
	queryset = Portfolio.objects.all()

	def get_queryset(self):
		return self.queryset.filter(title=title)

