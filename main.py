import sys,os
from os.path import dirname, join, abspath
from heapq import heappop, heappush, heapify
import time
import json
from ast import literal_eval

from trnxAncestor import TranxAncestor 
from common_utils.helpers import common_ut as common_util, custom_exception 
import common_utils.logger

logger = common_utils.logger.MyLogger(directory="/var/log/bitgo", category="script")

heap =[]
heapify(heap)

if __name__ == '__main__':
    try:

        start_time = time.perf_counter()

        bitgoExample = TranxAncestor(block_hight=680000)
        bitgoExample.get_block_hash()
        all_txids_in_block = bitgoExample.get_all_txids()
        total_txns = int(bitgoExample.get_total_tx_count())
        total_index = total_txns/int(25) # 25 is the rate limit as per the api  # TODO ip from commadn 
        index_count = 0

        while (index_count <= total_txns):
            raw_tx = bitgoExample.get_raw_trnx(index_count)
            
            if raw_tx:   ## why not if not 
                for single_tx_data in raw_tx:
                    parent_tx = single_tx_data.get('txid')
                    vin = single_tx_data.get("vin", [])

                    # whyt not recurssin here it self
                    for temp_data in vin:  # use prioper variables
                        raw_tx1=temp_data["txid"]
                        vout_int=temp_data["vout"]
                        if raw_tx1 in all_txids_in_block:
                            # Ancestry found
                            bitgoExample.calculate_ans.ancient_count=1  
                            bitgoExample.calculate_ans(bitgoExample.get_single_tx_detail(raw_tx1)) #calculate all parents recirsivly
                            heappush(heap, (-1 * (bitgoExample.calculate_ans.ancient_count),parent_tx))

            index_count += 25 # single point of truth
        
        c = 0
        while not c>10:
            ans = heappop(heap)
            print ("Ancestr Count : {} , txid: {}".format(int(ans[0]*(-1)),ans[1]) )
            c += 1

        end_time = time.perf_counter()
        print("Program Execution Time {} seconds".format(end_time - start_time))
        print("End oF the Code")

    except Exception as e:
        error = common_util.get_error_traceback(sys, e)
        logger.error_logger(error)
        raise
