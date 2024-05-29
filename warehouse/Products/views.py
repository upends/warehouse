from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .models import Product
from .serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

def warehouseLandingPage(request):
    return HttpResponse('Hi this is http response')


@api_view(['GET'])
def getAllProduct(request):
    products = Product.objects.all()
    serializedProductData = ProductSerializer(products, many=True).data
    return Response(serializedProductData)


@api_view(['GET'])
def getProduct(request, id):
    try:
        product = Product.objects.get(id=id)    
    except:
        return Response({"error":"Product dosn't exists"}, status=status.HTTP_404_NOT_FOUND)
    serializedProduct = ProductSerializer(product).data
    return Response(serializedProduct)


@api_view(['PATCH'])
def updateProduct(request, id):
    try:
        product = Product.objects.get(id=id)
    except:
        return Response({"error":"Product dosn't exists"}, status=status.HTTP_404_NOT_FOUND)

    serializedProduct = ProductSerializer(product, data=request.data, partial=True)
    if serializedProduct.is_valid():
        serializedProduct.save()
        return Response(serializedProduct.data)
    return Response(serializedProduct.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def createProduct(request):
    deserializedData = ProductSerializer(data=request.data)
    if deserializedData.is_valid():
        deserializedData.save()
        return Response(deserializedData.data, status=status.HTTP_201_CREATED)
    return Response(deserializedData.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def deleteProduct(request, id):
    try:
        product = Product.objects.get(id=id)
    except:
        return Response({"error" : "Product doesn't exists"}, status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response(status=status.HTTP_200_OK)