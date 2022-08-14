import sys,json
from ast import literal_eval
from common_utils.helpers import common_ut as common_util
import common_utils.logger
import ref_string

logger = common_utils.logger.MyLogger(directory="/var/log/bitgo", category="script")

class BtcBlock:

    def __init__(self,block_hight=0):
        self.block_hight = block_hight
        self.block_hash = None
        self.base_url = ref_string.EnvVariables.base_url
        self.all_txids_in_block= []

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


    def get_all_txids_in_block(self):
        '''
        return  list of transactions in given block hash
        '''
        try:
            if self.all_txids_in_block:
                return self.all_txids_in_block
            url = self.base_url+'block/{}/txids'.format(self.block_hash)
            all_txids_in_block = literal_eval(common_util.request_helper(url))
            self.all_txids_in_block = all_txids_in_block
            return all_txids_in_block

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

