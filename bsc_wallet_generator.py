from eth_account import Account
from mnemonic import Mnemonic

def create_bsc_wallets(total=5):
    mnemo = Mnemonic("english")
    Account.enable_unaudited_hdwallet_features()
    
    for i in range(total):
        words = mnemo.generate(128)
        wallet = Account.from_mnemonic(words)
        print(f"BSC钱包 {i+1}")
        print(f"助记词: {words}")
        print(f"地址: {wallet.address}")
        print(f"私钥: {wallet.key.hex()}\n")

if __name__ == "__main__":
    create_bsc_wallets(2)
