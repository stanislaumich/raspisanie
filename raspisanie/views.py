import locale

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from alert.models import Alert
from mess.models import Mess
from person.models import Person
from person.serializers import PersonSerializer
from raspisanie.settings import BASE_DIR

locale.setlocale(locale.LC_ALL, "")


def index(request):
    uid = request.session.get('userid', 0)
    mes = Mess.objects.filter(toid=uid, isActive=1).all().order_by('-id')
    mesmy = Mess.objects.filter(fromid=uid, isActive=1).all().order_by('-id')
    messys = Alert.objects.filter(toid=uid, isActive=1).all().order_by('-id')
    data = {'a': 'fio', 'mes': mes, 'mesmy': mesmy, 'messys': messys}
    return render(request, "index.html", context=data)


# ---------------------------------

@api_view(['GET', 'POST'])
def person_list(request):
    if request.method == 'GET':
        data = Person.objects.all()
        serializer = PersonSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print('post')
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE', 'GET'])
def person_detail(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'GET':
        person = Person.objects.get(pk=pk)
        serializer = PersonSerializer(person, context={'request': request}, many=False)
        return Response(serializer.data)


def test(request):
    with open('s:\\django\\raspisanie\\templates\\test.html', 'r') as file:
        data = file.read().replace('\n', '\n')
    return HttpResponse(data)
