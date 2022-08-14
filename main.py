import sys, time
from heapq import heappop, heappush, heapify
from btc_block import logger, BtcBlock
from common_utils.helpers import common_ut as common_util
import ref_string

heap = []
heapify(heap)
all_txids_in_block = []

def calculate_anscestor(single_tx_data):
    """
    recursive function to calculate total number of ancestors
    """
    try:
        global all_txids_in_block
        vin = single_tx_data["vin"]
        for vin_data in vin:
            raw_tx1=vin_data["txid"]
            if raw_tx1 in  all_txids_in_block:
                calculate_anscestor.ancient_count += 1
                calculate_anscestor(BtcBlock.get_single_tx_detail(raw_tx1))
            return 0
    except Exception as e:
        error = common_util.get_error_traceback(sys, e)
        logger.error_logger(error)
        raise

 
def main():
    try:
        global all_txids_in_block

        bitgoExample =  BtcBlock(block_hight=ref_string.EnvVariables.crawl_block_height)
        bitgoExample.get_block_hash()
        all_txids_in_block = bitgoExample.get_all_txids_in_block()
        total_txns = int(bitgoExample.get_total_tx_count())
        index_count = 0

        while (index_count <= total_txns):
            raw_tx = bitgoExample.get_raw_trnx(index_count)
            
            if raw_tx:  
                for single_tx_data in raw_tx:
                    parent_tx = single_tx_data.get('txid')
                    vin = single_tx_data.get("vin", [])

                    for vin_data in vin: 
                        raw_tx1=vin_data["txid"]
                        if raw_tx1 in all_txids_in_block:
                            # Ancestry found
                            calculate_anscestor.ancient_count=1  
                            calculate_anscestor(bitgoExample.get_single_tx_detail(raw_tx1)) #calculate all parents recirsivly
                            heappush(heap, (-1 * (calculate_anscestor.ancient_count),parent_tx))

            index_count += ref_string.EnvVariables.api_trnx_detail_limit
        
        output_count = 0
        while output_count > ref_string.EnvVariables.limit_to_show_op:
            ancestor_family = heappop(heap)
            print ("Ancestr Count : {} , txid: {}".format(int(ancestor_family[0]*(-1)),ancestor_family[1]) )
            output_count += 1

    except Exception as e:
        error = common_util.get_error_traceback(sys, e)
        logger.error_logger(error)
        raise

if __name__ == '__main__':
    try:
        start_time = time.perf_counter()
        main()
        end_time = time.perf_counter()
        print("Program Execution Time {} seconds".format(end_time - start_time))
        print("End oF the Code")

    except Exception as e:
        error = common_util.get_error_traceback(sys, e)
        logger.error_logger(error)
