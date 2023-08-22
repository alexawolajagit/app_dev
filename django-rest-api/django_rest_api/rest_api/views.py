from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Data
from .serializers import DataSerializer 
# Create your views here.
@api_view(['GET'])
def getApi(request):
    info = Data.objects.all()
    serializer = DataSerializer(info, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postApi(request):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)