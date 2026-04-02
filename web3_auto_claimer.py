from web3 import Web3
import time

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))
YOUR_KEY = "你的私钥"
YOUR_ADDR = w3.eth.account.from_key(YOUR_KEY).address

def auto_claim(contract_addr):
    print("自动任务领取运行中...")
    while True:
        print(f"{time.ctime()} | 检查可领取奖励")
        time.sleep(60)

if __name__ == "__main__":
    auto_claim("0x...合约地址")
