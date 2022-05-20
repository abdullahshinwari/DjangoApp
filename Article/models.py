from django.db import models

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)


class Articles(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)


class Blocks(models.Model):
    block_number = models.BigIntegerField()  # "10001000",
    block_timestamp = models.DateTimeField()  # "2020-05-04T17:09:31.000Z",
    block_hash = models.CharField(max_length=200)  # "0x491123638754d9e1b9615c19603c8b25a48b0e3297be1330c5902b6f4a31a212",
    transaction_hash = models.CharField(max_length=200)  # "0x07faec273f41f3488828aeae2c55b1284abd0c8d925f67a9dbde95cb8dc917c5",
    transaction_index = models.IntegerField(default=False)  # 149,
    log_index = models.IntegerField(default=False)  # 162,
    value = models.BigIntegerField(default=False)  # "50000000000000000",
    contract_type = models.CharField(max_length=200)  # "ERC721",
    transaction_type = models.CharField(max_length=200)  # "Single",
    token_address = models.CharField(max_length=200)  # "0xebfe22c48a5d9707a1be9c668e0638f271efa43b",
    token_id = models.IntegerField(default=False)  # "1726",
    from_address = models.CharField(max_length=200)  # "0x7fc95edd03d58ba010c8be25b03d4940b39cc97e",
    to_address = models.CharField(max_length=200)  # "0xdfd1503bff6ca15b573cca1c8665b01e4c032b2a",
    amount = models.CharField(max_length=200)  # "1",
    verified = models.IntegerField(default=False)  # 1,
    operator = models.CharField(max_length=200)  # null
