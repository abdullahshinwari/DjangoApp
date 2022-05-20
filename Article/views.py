import requests

from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from Article.models import Users, Articles, Blocks
from Article.serializers import UsersSerializer, ArticlesSerializer, BlocksSerializer
from utils import to_json
from Article.utils import get_block_page


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


# call moralis api
@api_view(["POST"])
def moralis_api(request):
    try:
        keep_fetching = True
        from_block = request.POST['from_block']
        to_block = request.POST['to_block']
        response = get_block_page(from_block, to_block)
        while keep_fetching:
            print(response['cursor'])
            if response['cursor']:
                response = get_block_page(from_block, to_block, response['cursor'])
                continue
            keep_fetching = False
        return Response({"message": "database is populated !!!"})


        # api_key = 'KxNtf5bwDTmZ9ucCxXLv1l9cuFTSAiR4xPetY6n6l2rboWUqQjMyQJ0eBcgBNAoe'
        # url = ('https://deep-index.moralis.io/api/v2/nft/transfers?chain=eth&from_block=10000000&to_block=10001000&format=decimal')
        #
        # all_blocks = []
        # response = requests.get(url=url, headers={"X-API-Key": api_key})
        # if response.status_code != 200:
        #     return to_json(data="", message='Error', status_code=400)  # dummy status code
        # block_data = response.json()
        # for block in block_data['result']:
        #     all_blocks.append(Blocks(
        #         block_number=block['block_number'],
        #         block_timestamp=block['block_timestamp'],
        #         block_hash=block['block_hash'],
        #         transaction_hash=block['transaction_hash'],
        #         transaction_index=block['transaction_index'],
        #         log_index=block['log_index'],
        #         value=block['value'],
        #         contract_type=block['contract_type'],
        #         transaction_type=block['transaction_type'],
        #         token_address=block['token_address'],
        #         token_id=block['token_id'],
        #         from_address=block['from_address'],
        #         to_address=block['to_address'],
        #         amount=block['amount'],
        #         verified=block['verified'],
        #         operator=block['operator']
        #     ))
        #     # if block_serializer.is_valid():
        #     #     block_serializer.save()
        # Blocks.objects.bulk_create(all_blocks, ignore_conflicts=True)
        # print('after append')
    except ConnectionError as e:
        return to_json(data="", message=e, status_code=400)  # dummy status code
    # return Response({"data": "all_blocks"})



