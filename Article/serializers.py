from rest_framework import serializers
from Article.models import Users, Articles, Blocks


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('name', 'username', 'password')


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('title', 'description')


class BlocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blocks
        fields = ('block_number', 'block_timestamp', 'block_hash', 'transaction_hash', 'transaction_index', 'log_index',
                  'value', 'contract_type', 'transaction_type', 'token_address', 'token_id', 'from_address',
                  'to_address', 'amount', 'verified', 'operator')
