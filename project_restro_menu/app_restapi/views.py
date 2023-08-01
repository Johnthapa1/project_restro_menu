from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from app_restapi.serializers import CategorySerializer, MenuSerializer
from app_menus.models import Menu, Category

# Create your views here.
class CustomResponse():
    def get_success(self, code, msg, data):
        context = {
            "status_code": code,
            "message": msg,
            "data": data,
            "error": {}
        }
        return context

    def get_error(self, code, msg, error):
        context = {
            "status_code": code,
            "message": msg,
            "data": {},
            "error": error
        }
        return context

class CategoryApiView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        res = CustomResponse()
        return Response(res.get_success(200, "Category List", serializer.data), status=status.HTTP_200_OK)
    
    def post(self, request):
        req_data = request.data # must be a json request
        serializer = CategorySerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryApiIdView(APIView):
    def get_object(self, id):
        try:
            category = Category.objects.get(id=id)
            return category
        except Category.DoesNotExist:
            return None

    def get(self, request, id):
        instance = self.get_object(id)
        res = CustomResponse()

        if instance is None:
            return Response(res.get_error(404, "Data not found", {"msg": "Data not found"}), status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(instance)

        return Response(res.get_success(200, "Category Details", serializer.data), status=status.HTTP_200_OK)

    def put(self, request, id):
        instance = self.get_object(id)
        res = CustomResponse()

        if instance is None:
            return Response(res.get_error(404, "Data not found", {"msg": "Data not found"}), status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(res.get_success(200, "Data updated", serializer.data), status=status.HTTP_200_OK)
        return Response(res.get_error(400, "Something went wrong", serializer.errors), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        instance = self.get_object(id)
        if instance is None:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"msg": "Data deleted successfully"}, status=status.HTTP_200_OK)

class MenuApiView(APIView):
    def get(self, request):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        req_data = request.data # must be a json request
        serializer = MenuSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuApiIdView(APIView):
    def get_object(self, id):
        try:
            menu = Menu.objects.get(id=id)
            return menu
        except Menu.DoesNotExist:
            return None

    def get(self, request, id):
        instance = self.get_object(id)
        if instance is None:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MenuSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        instance = self.get_object(id)
        if instance is None:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MenuSerializer(instance=instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        instance = self.get_object(id)
        if instance is None:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"msg": "Data deleted successfully"}, status=status.HTTP_200_OK)