from rest_framework import serializers
from .models import Person, MyPers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'fio', 'fam', 'name', 'otch', 'born', 'dolg', 'isAdmin')


class MyPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id',  'fio', 'fam', 'name', 'otch', 'born', 'dolg', 'isAdmin') #('__all__') #,
