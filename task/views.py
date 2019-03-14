from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import task
from . serializers import taskSerializer
from django.http import QueryDict

class tasklist(APIView):
        def get(self,request):
                task1 = task.objects.all()
                serializer = taskSerializer(task1,many=True)
                return Response(serializer.data)
                
        def post(self,request):
            print(request.POST.get('mode'))
            if request.POST.get('mode')=='1':
                print(request.POST.get('mode'))
                name = request.POST.get('name', '')
                mark = 0
                date = request.POST.get('date', '')
                description = request.POST.get('description', '')
                c = task(task_name=name, mark_complete = 0, description=description, closed_date = date)
                c.save()
            if request.POST.get('mode')=='2':
                task.objects.get(id=request.POST.get('id')).delete()
                print("mode 2")
                
            if request.POST.get('mode')=='3':
                c = task.objects.get(id=request.POST.get('id'))
                c.name = request.POST.get('name', '')
                c.mark = request.POST.get('mark')
                # c.date = request.POST.get('closed_date', '')
                c.description = request.POST.get('description', '')
                print("mode 3")
                c.save()
        

