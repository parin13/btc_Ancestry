import sys,os
from os.path import dirname, join, abspath
import datetime
import requests
import json
from ast import literal_eval

from common_utils.helpers import common_ut as common_util, custom_exception
import common_utils.logger

log_dir = "/var/log/bitgo"
log_category="script"

logger = common_utils.logger.MyLogger(log_dir, log_category)


base_url = "https://blockstream.info/api/"
block_hash="000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732"
 

def get_total_tx_count(block_hash):
    '''
    calculate the total no of transcaction in the given block
    '''
    try:
        url = base_url+'block/{}'.format(block_hash)
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.content.decode('UTF-8')).get("tx_count",0)
            return(data)

    except Exception as e:
        error = common_util.get_error_traceback(sys, e)
        logger.error_logger(error)
        raise


def get_all_txids(block_hash):
    '''
    return list of total transaction in given block
    '''

    try:
        url = base_url+'block/{}/txids'.format(block_hash)
        response = requests.get(url)
        if response.status_code == 200:
            data = literal_eval(response.content.decode('UTF-8'))
            return data

    except Exception as e:
        error = common_util.get_error_traceback(sys, e)
        logger.error_logger(error)
        raise


def get_raw_trnx(index_count):
    """
    Returns transaction information given block:
    """
    try:
        url = base_url+'block/{}/txs/{}'.format(block_hash,index_count)
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.content.decode('UTF-8'))
            return data
    except Exception as e:
        error = common_util.get_error_traceback(sys, e)
        logger.error_logger(error)
        raise


    except Exception as e:
        error = common_util.get_error_traceback(sys, e)
        logger.error_logger(error)
        raise


def main():
    """
    Entry Point
    :return:
    """
    try:
        block_number = 680000
        all_txids_in_block = get_all_txids(block_hash) # returns array 
        total_txns = int(get_total_tx_count(block_hash))
        total_index = total_txns/int(25) # 25 is the rate limit as per the api
        index_count = 0
        final_count = 0
        while (index_count <= total_txns):
            raw_tx = get_raw_trnx(index_count)
            if raw_tx:
                for single_tx_data in raw_tx:
                    vin = single_tx_data["vin"]
                    for temp_data in vin:
                        raw_tx1=temp_data["txid"]
                        vout_int=temp_data["vout"]
                        if raw_tx1 in all_txids_in_block:
                            #this is  vin addresa and vout address
                            # vin_add = vin_address(raw_tx1)
                            final_count = final_count+1
                index_count += 25

        
        print ("Total count  is :",final_count)   #final_count = 389
        raise

    except Exception as e:
        error = common_util.get_error_traceback(sys, e)
        logger.error_logger(error)
        raise



if __name__ == '__main__':
    main()