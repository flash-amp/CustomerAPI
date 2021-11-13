from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def Customers(request):

    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    elif request.method == 'POST' :
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET','PUT','DELETE'])
def Specific_Customer(request,id):
    customer = get_object_or_404(Customer,id=id)
    if request.method == 'GET' :
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    elif request.method == 'PUT' :
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(customer,data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE' :
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
