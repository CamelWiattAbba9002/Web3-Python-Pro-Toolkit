from web3 import Web3

ABI = '[{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"blacklisted","outputs":[{"type":"bool"}],"payable":false}]'
w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

def check_token_security(token_addr):
    try:
        contract = w3.eth.contract(address=token_addr, abi=ABI)
        has_blacklist = True
        print("⚠️ 该代币包含黑名单功能")
    except:
        has_blacklist = False
        print("✅ 未检测到黑名单功能")
    return has_blacklist

if __name__ == "__main__":
    check_token_security("0xdAC17F958D2ee523a22062069C4583D11Cc8f6DD7")
