#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Branches, Banks

class BanksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Banks
        fields = ['id', 'name']


class BranchesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branches
        fields = ['ifsc', 'bank_id', 'branch', 'address','city','district','state']