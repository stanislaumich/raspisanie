from rest_framework import serializers
from .models import Person


# class StudentSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Student
#         fields = ('pk', 'name', 'email', 'document', 'phone', 'registrationDate','photo')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('fio', 'fam', 'name', 'otch', 'born', 'dolg', 'isAdmin')
