BTC Transaction Ancestry Sets


To calculate transaction Ancestor

My Approach :

Find out the total transaction Ids in the block
Iterate over all trnx ids and find out if any trnx has an ancestor in the same block (simple vin vout calculation)
Recursively Call over all ancestors and store a count
Maintain max heap of ancestor counts and associate each of them with leaf level transaction Ids
pop out the new heap to get Ancestors in decreasing order



Code Structure:
Entry Point: main.py : Contains all the business logics part
Dependency: Common_ut.py: Contains common modules like error traceback, logger, request helpers etc
Input Block Height: 680000


Here are the top 10 transactions with their ancestors :
Ancestr Count : 14 , txid: 7d08f0c61cda9379bdf1fa68095f827199a0d4cb6b466a6da3f0dc956772c52b
Ancestr Count : 13 , txid: b2bab595112517e8b6a06aa9f616272b479e57e21b4da52877ddf385316aa19b
Ancestr Count : 12 , txid: 4205c68c68266259c5723948e0407dff25600e6420659cef4286dd1ae4658b63
Ancestr Count : 12 , txid: 7841dc7cf61d394094f4341fa98d0a6fd771e95ac93a9dcfec12a23ed3c670c5
Ancestr Count : 12 , txid: 7a128b0242d89d327fc2c273199c7529a31477d8ea949e5176b2a4eb69b74464
Ancestr Count : 12 , txid: d294be35db0b5fab4a6a00d6e4441c7e54be88fa02dfc188b75e4604ec6c3fcf
Ancestr Count : 11 , txid: 4b4c90943c1651eabb8c5dfb6f490c4e56bd6cf42950a0430db17b9691b0236c
Ancestr Count : 11 , txid: 973e5adb05cc1cb80cabc5e451200333c993034153a078733ec06af7bf3c860b
Ancestr Count : 11 , txid: afe4b90e667df0171f63e6cc95c0a12d24592d436dd2e8b9b2a9998b4099ff6d
Ancestr Count : 11 , txid: ef6c8e97b62eced1913df503667d49b9f5890cdb201be5d5d6c304af1d3f5db1
Ancestr Count : 10 , txid: 0ad457d555ad80f8823027d892547b403f807529a31bfb4ff205e836052c7e4dMain Features of my codebase:

Features: 

Logger implementation
Custom Exception
Modular code with OOps concept
Structural Analysis of codebase
