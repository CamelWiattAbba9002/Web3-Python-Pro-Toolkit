from web3 import Web3

def check_multi_chain(chain, address):
    rpc = {
        "eth": "https://rpc.ankr.com/eth",
        "bsc": "https://bsc-dataseed1.binance.org/",
        "polygon": "https://polygon-rpc.com"
    }
    w3 = Web3(Web3.HTTPProvider(rpc[chain]))
    bal = w3.from_wei(w3.eth.get_balance(address), 'ether')
    print(f"{chain.upper()} 余额: {bal:.4f}")

if __name__ == "__main__":
    addr = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
    check_multi_chain("eth", addr)
    check_multi_chain("bsc", addr)
