from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from Article.models import Users, Articles
from Article.serializers import UsersSerializer, ArticlesSerializer

# Create your views here.


# print hello world message api
@api_view(["GET"])
def hello_world(request):
    return Response({'message': 'Hello World!!!'})


@api_view(["POST"])
def create_user(request):
    try:
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
    except:
        return Response({'message': 'name, username or password is missing !!!'})
    user = Users.objects.create(name=name, username=username, password=password)
    user.save()
    return Response({'Message': 'user successfully created !!!'})


@api_view(["GET"])
def show_user(request):
    try:
        id_ = request.POST['id']
    except:
        return Response({'message': 'id is missing !!!'})
    user = Users.objects.get(id=id_)
    user_serializer = UsersSerializer(user)
    return JsonResponse(user_serializer.data, safe=False)


@api_view(["GET"])
def show_all_users(request):
    users = Users.objects.all()
    users_serializer = UsersSerializer(users)
    return JsonResponse(users_serializer, safe=False)


@api_view(["PUT"])
def update_user(request):
    user_data = JSONParser().parse(request)
    user= Users.objects.get(id=user_data['id'])
    user_serializer = UsersSerializer(user, data=user_data)
    if user_serializer.is_valid():
        user_serializer.save()
        return JsonResponse("Updated Successfully", safe=False)
    return JsonResponse("Failed to Update", safe=False)


@api_view(["DELETE"])
def delete_user(request):
    try:
        id_ = request.POST['id']
    except:
        return Response({'message': 'id is missing !!!'})
    user = Users.objects.get(id=id_)
    user.delete()
    return JsonResponse("Deleted Successfully", safe=False)

