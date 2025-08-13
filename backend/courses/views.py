# backend/courses/views.py
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer

class CategoryListView(generics.ListAPIView):
    """List all active categories."""
    queryset = Category.objects.filter(is_active=True).order_by('name')
    serializer_class = CategorySerializer
