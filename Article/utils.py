import requests

from rest_framework.response import Response
from django.http.response import JsonResponse

from utils import to_json
from Article.models import Blocks


def get_block_page(from_block, to_block, cursor=''):
    print('get_block_page is called !!!')
    api_key = 'KxNtf5bwDTmZ9ucCxXLv1l9cuFTSAiR4xPetY6n6l2rboWUqQjMyQJ0eBcgBNAoe'
    url = ('https://deep-index.moralis.io/api/v2/nft/transfers?chain=eth&'
           'from_block={from_block}&to_block={to_block}&format=decimal')
    url = url.format(from_block=from_block, to_block=to_block)
    if cursor != '':
        url = url + '&cursor=' + cursor
    all_blocks = []
    print(url)
    response = requests.get(url=url, headers={"X-API-Key": api_key})
    if response.status_code != 200:
        return to_json(data="", message='Error', status_code=400)  # dummy status code
    block_data = response.json()
    for block in block_data['result']:
        all_blocks.append(Blocks(
            block_number=block['block_number'],
            block_timestamp=block['block_timestamp'],
            block_hash=block['block_hash'],
            transaction_hash=block['transaction_hash'],
            transaction_index=block['transaction_index'],
            log_index=block['log_index'],
            value=block['value'],
            contract_type=block['contract_type'],
            transaction_type=block['transaction_type'],
            token_address=block['token_address'],
            token_id=block['token_id'],
            from_address=block['from_address'],
            to_address=block['to_address'],
            amount=block['amount'],
            verified=block['verified'],
            operator=block['operator']
        ))
    Blocks.objects.bulk_create(all_blocks, ignore_conflicts=True)
    return block_data
