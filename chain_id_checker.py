from web3 import Web3

RPC_LIST = {
    "ETH": "https://rpc.ankr.com/eth",
    "BSC": "https://bsc-dataseed1.binance.org/",
    "Polygon": "https://polygon-rpc.com"
}

def get_chain_id(chain_name):
    w3 = Web3(Web3.HTTPProvider(RPC_LIST[chain_name]))
    cid = w3.eth.chain_id
    print(f"{chain_name} ChainID: {cid}")
    return cid

if __name__ == "__main__":
    get_chain_id("ETH")
    get_chain_id("BSC")
