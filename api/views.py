from django.shortcuts import render

# Create your views here.
# Create your views here.
#from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BanksSerializer, BranchesSerializer
from .models import Banks, Branches


class BanksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Banks.objects.all().order_by('id')
    serializer_class = BanksSerializer
    permission_classes = [permissions.IsAuthenticated]


class BranchesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer
    permission_classes = [permissions.IsAuthenticated]