import sys,os
from os.path import dirname, join, abspath
from heapq import heappop, heappush, heapify
import datetime
import requests
import json
from ast import literal_eval

from common_utils.helpers import common_ut as common_util, custom_exception 
import common_utils.logger

logger = common_utils.logger.MyLogger(directory="/var/log/bitgo", category="script")

heap =[]
heapify(heap)

class TranxAncestor:

    def __init__(self,block_hash=None):
        self.block = 680000
        self.block_hash = block_hash
        self.base_url = "https://blockstream.info/api/"

    def get_total_tx_count(self):
        '''
        calculate the total no of transcaction in the given block
        '''
        try:
            url = self.base_url+'block/{}'.format(self.block_hash)
            response = requests.get(url)
            if response.status_code == 200:
                data = json.loads(response.content.decode('UTF-8')).get("tx_count",0)
                return(data)

        except Exception as e:
            error = common_util.get_error_traceback(sys, e)
            logger.error_logger(error)
            raise


    def get_all_txids(self):
        '''
        return list of total transaction in given block
        '''

        try:
            url = self.base_url+'block/{}/txids'.format(self.block_hash)
            response = requests.get(url)
            if response.status_code == 200:
                data = literal_eval(response.content.decode('UTF-8'))
                return data

        except Exception as e:
            error = common_util.get_error_traceback(sys, e)
            logger.error_logger(error)
            raise

    @staticmethod
    def get_raw_trnx(block_hash,index_count):
        """
        Returns transaction information given block:
        """
        try:
            base_url = 'https://blockstream.info/api/'
            url = base_url+'block/{}/txs/{}'.format(block_hash,index_count)
            response = requests.get(url)
            if response.status_code == 200:
                data = json.loads(response.content.decode('UTF-8'))
                return data
        except Exception as e:
            error = common_util.get_error_traceback(sys, e)
            logger.error_logger(error)
            raise

    @staticmethod
    def get_single_tx_detail(txid):
        try:
            base_url = 'https://blockstream.info/api/'
            url = base_url+'tx/{}'.format(txid)
            response = requests.get(url)
            if response.status_code == 200:
                data = json.loads(response.content.decode('UTF-8'))
                return data
        except Exception as e:
            error = common_util.get_error_traceback(sys, e)
            logger.error_logger(error)
            raise


def calculate_ans(single_tx_data):
    try:
        vin = single_tx_data["vin"]
        for temp_data in vin:
            raw_tx1=temp_data["txid"]
            vout_int=temp_data["vout"]
            if raw_tx1 in all_txids_in_block:
                calculate_ans.ancient_count += 1
                calculate_ans(bitgoExample.get_single_tx_detail(raw_tx1))
            return 0
    except Exception as e:
        error = common_util.get_error_traceback(sys, e)
        logger.error_logger(error)
        raise


if __name__ == '__main__':
    bitgoExample = TranxAncestor("000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732") #pre calculate the block hash

    all_txids_in_block = bitgoExample.get_all_txids()
    total_txns = int(bitgoExample.get_total_tx_count())
    total_index = total_txns/int(25) # 25 is the rate limit as per the api
    index_count = 0
    ancenstry_count = 0
    while (index_count <= total_txns):
        raw_tx = bitgoExample.get_raw_trnx(bitgoExample.block_hash,index_count)
        
        if raw_tx:
            for single_tx_data in raw_tx:
                parent_tx = single_tx_data.get('txid')
                vin = single_tx_data["vin"]
                for temp_data in vin:
                    raw_tx1=temp_data["txid"]
                    vout_int=temp_data["vout"]
                    if raw_tx1 in all_txids_in_block:
                        # Ancestry found
                        calculate_ans.ancient_count=1
                        calculate_ans(bitgoExample.get_single_tx_detail(raw_tx1)) #calculate all parents recirsivly
                        heappush(heap, (-1 * (calculate_ans.ancient_count),parent_tx))
                        ancenstry_count = ancenstry_count+1
        index_count += 25
    
    c = 0
    abc = heap
    while not c>10:
        print(heappop(heap))
        c += 1    
