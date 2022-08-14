import sys,os
from os.path import dirname, join, abspath
from heapq import heappop, heappush, heapify
import time
import json
from ast import literal_eval

from common_utils.helpers import common_ut as common_util, custom_exception 
import common_utils.logger

logger = common_utils.logger.MyLogger(directory="/var/log/bitgo", category="script")



class TranxAncestor:

    def __init__(self,block_hight=0):
        self.block_hight = block_hight
        self.block_hash = None
        self.base_url = "https://blockstream.info/api/"

    def get_block_hash(self):
        """
        Returns Block has for provided block height
        """
        try:
            url = self.base_url+'block-height/{}'.format(self.block_hight)
            self.block_hash = common_util.request_helper(url)


        except Exception as e:
            error = common_util.get_error_traceback(sys, e)
            logger.error_logger(error)
            raise


    def get_total_tx_count(self):
        '''
        calculate the total no of transcaction in the given block
        '''
        try:
            url = self.base_url+'block/{}'.format(self.block_hash)
            response = common_util.request_helper(url)
            return json.loads(response).get("tx_count",0)

        except Exception as e:
            error = common_util.get_error_traceback(sys, e)
            logger.error_logger(error)
            raise


    def get_all_txids(self):
        '''
        return  list of transactions in given block hash
        '''
        try:
            url = self.base_url+'block/{}/txids'.format(self.block_hash)
            return literal_eval(common_util.request_helper(url))

        except Exception as e:
            error = common_util.get_error_traceback(sys, e)
            logger.error_logger(error)
            raise

    
    def get_raw_trnx(self,index_count):
        """
        Returns transaction information for given block hash:
        """
        try:
            url = self.base_url+'block/{}/txs/{}'.format(self.block_hash,index_count)
            response = common_util.request_helper(url)
            if response:
                return json.loads(response)

        except Exception as e:
            error = common_util.get_error_traceback(sys, e)
            logger.error_logger(error)
            raise

    @staticmethod
    def get_single_tx_detail(txid):
        """ 
        GIves transaction detail as per provided Txid
        """
        try:
            base_url = 'https://blockstream.info/api/'
            url = base_url+'tx/{}'.format(txid)
            response = common_util.request_helper(url)
            return json.loads(response)

        except Exception as e:
            error = common_util.get_error_traceback(sys, e)
            logger.error_logger(error)
            raise

    @staticmethod
    def calculate_ans(single_tx_data):
        """
        recursive function to calculate total number of ancestors
        """
        try:
            vin = single_tx_data["vin"]
            for temp_data in vin:
                raw_tx1=temp_data["txid"]
                vout_int=temp_data["vout"]
                if raw_tx1 in all_txids_in_block:
                    bitgoExample.calculate_ans.ancient_count += 1
                    bitgoExample.calculate_ans(bitgoExample.get_single_tx_detail(raw_tx1))
                return 0
        except Exception as e:
            error = common_util.get_error_traceback(sys, e)
            logger.error_logger(error)
            raise

