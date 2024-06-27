from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'fio', 'fam', 'name', 'otch', 'born', 'dolg', 'isAdmin')
