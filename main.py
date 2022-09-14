import codecs
import datetime
import io
import json
from os import path
import string
import subprocess
import time
from types import NoneType

import requests
from web3 import Web3
import tweepy
import panoramix

import re


infura_url = 'https://mainnet.infura.io/v3/'

infura_url2 = 'https://mainnet.infura.io/v3/'

infura_url3 = 'https://mainnet.infura.io/v3/'

alchemy_url ='https://eth-mainnet.g.alchemy.com/v2/'

quicknode_url = ''



web3 = Web3(Web3.HTTPProvider(alchemy_url))

abi = json.loads('[{"inputs":[{"internalType":"contract ENS","name":"_ens","type":"address"},{"internalType":"bytes32","name":"_baseNode","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"controller","type":"address"}],"name":"ControllerAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"controller","type":"address"}],"name":"ControllerRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"expires","type":"uint256"}],"name":"NameMigrated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"expires","type":"uint256"}],"name":"NameRegistered","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"expires","type":"uint256"}],"name":"NameRenewed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"GRACE_PERIOD","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"controller","type":"address"}],"name":"addController","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"available","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"baseNode","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"controllers","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"ens","outputs":[{"internalType":"contract ENS","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"nameExpires","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"owner","type":"address"}],"name":"reclaim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"duration","type":"uint256"}],"name":"register","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"duration","type":"uint256"}],"name":"registerOnly","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"controller","type":"address"}],"name":"removeController","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"duration","type":"uint256"}],"name":"renew","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"resolver","type":"address"}],"name":"setResolver","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes4","name":"interfaceID","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')

ETHERSCAN_API_KEY = ""


def get_last_block():
    return int(json.loads(requests.get(
        f"https://api.etherscan.io/api?module=block&action=getblocknobytime&timestamp={round(time.time())}&closest=before&apikey={ETHERSCAN_API_KEY}"
    ).text)["result"])

def get_last_txs(since=2):
    print(str(get_last_block()) + '<- Block Number')
    txs = json.loads(requests.get(
        f"https://api.etherscan.io/api?module=account&action=tokennfttx&contractaddress={addy}&startblock={get_last_block() - 15}&sort=asc&apikey={ETHERSCAN_API_KEY}"
    ).text)["result"] 

    print(txs)
    return txs


def get_tx_block(block):
    tx_length = web3.eth.get_block_transaction_count(block)
    block = int(block)

    if tx_length == 0:
        return

    for j in range(0, tx_length):
        raw_tx = web3.eth.get_transaction_by_block(block, j)
        

        #time.sleep(.3)
   
        parsed_tx = toDict(raw_tx)
        tx_hash = str(parsed_tx['hash'])


        raw_receipt = web3.eth.get_transaction_receipt(tx_hash)
        parsed_receipt = toDict(raw_receipt)


        to_value = parsed_tx['to']




        if type(to_value) == NoneType:
            contract_address = str(parsed_receipt['contractAddress'])

            hex_bytes = web3.eth.getCode(contract_address)
            bytecode = str(hex_bytes.hex())

            

            save_tx(tx_hash, block, contract_address)
            decompile_contract(bytecode, contract_address, block)
            print("Winner: ", block, int(j))
    return
        

def toDict(dictToParse):
    # convert any 'AttributeDict' type found to 'dict'
    parsedDict = dict(dictToParse)
    for key, val in parsedDict.items():
        if 'list' in str(type(val)):
            parsedDict[key] = [_parseValue(x) for x in val]
        else:
            parsedDict[key] = _parseValue(val)
    return parsedDict


def _parseValue(val):
    # check for nested dict structures to iterate through
    if 'dict' in str(type(val)).lower():
        return toDict(val)
    # convert 'HexBytes' type to 'str'
    elif 'HexBytes' in str(type(val)):
        return val.hex()
    else:
        return val



def save_tx(hash, block, contract_address):
    with open('C:/Users/mason/Desktop/archeology/findings.json', 'r') as fp:
        information = json.load(fp)

    information.append({
        "contract_address": contract_address,
        "tx": hash,
        "block": block,
    })

    with open('C:/Users/mason/Desktop/archeology/findings.json', 'w') as fp:
        json.dump(information, fp, indent=2)
        fp.close()

    return()



def decompile_contract(bytecode, contract_address, block):
    decompile_contract = subprocess.check_output(["panoramix", bytecode], stderr=subprocess.DEVNULL)

    ansi_escape_8bit = re.compile(
    br'(?:\x1B[@-Z\\-_]|[\x80-\x9A\x9C-\x9F]|(?:\x1B\[|\x9B)[0-?]*[ -/]*[@-~])'
    )

    result = ansi_escape_8bit.sub(b'', decompile_contract).strip()

    result_decompile = result.decode("utf-8")

    contract_txt = 'contracts/' + str(block) + '__' + str(contract_address) + '.txt'

    text_file = open(contract_txt, "w")
    text_file.write(str(result_decompile))
    text_file.close()

    return()


def loop_blocks():
    for i in range(444371, 450000):
        get_tx_block(i)
        print('Analyzing block # ', i)
        #time.sleep(.1)


loop_blocks()

