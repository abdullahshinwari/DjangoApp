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
        user_data = JSONParser().parse(request)
        user_serializer = UsersSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse('user successfully created !!!', safe=False)
    except:
        return JsonResponse('Failed to add User !!!', safe=False)


@api_view(["GET"])
def show_user(request):
    try:
        id_ = request.POST['id']
        user = Users.objects.get(id=id_)
    except:
        return Response({'message': 'id is missing !!!'})
    user_serializer = UsersSerializer(user)
    return JsonResponse(user_serializer.data, safe=False)


@api_view(["GET"])
def show_all_users(request):
    users = Users.objects.all()
    users_serializer = UsersSerializer(users, many=True)
    # print(users.query) // to print raw sql query
    return JsonResponse(users_serializer.data, safe=False)


@api_view(["PUT"])
def update_user(request):
    user_data = JSONParser().parse(request)
    user = Users.objects.get(id=user_data['id'])
    user_serializer = UsersSerializer(user, data=user_data)
    if user_serializer.is_valid():
        user_serializer.save()
        return JsonResponse("Updated Successfully", safe=False)
    return JsonResponse("Failed to Update", safe=False)


@api_view(["DELETE"])
def delete_user(request):
    try:
        id_ = request.POST['id']
        user = Users.objects.get(id=id_)
    except:
        return Response({'message': 'id is missing !!!'})
    user.delete()
    return JsonResponse("Deleted Successfully", safe=False)

