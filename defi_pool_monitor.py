import requests
import time

def monitor_uniswap_pool(pool_addr):
    while True:
        data = requests.get(f"https://api.dexscreener.com/latest/dex/pairs/eth/{pool_addr}", timeout=10).json()
        price = data['pair']['priceUsd']
        liquidity = data['pair']['liquidity']['usd']
        print(f"价格: ${price} | 流动性: ${liquidity} | {time.ctime()}")
        time.sleep(10)

if __name__ == "__main__":
    monitor_uniswap_pool("0x88e6a0c2ddd26ea49ea6f84f2f400ec58eee0165")
