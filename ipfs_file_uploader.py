import requests

def upload_to_ipfs(file_path):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers = {"pinata_api_key": "你的KEY", "pinata_secret_api_key": "你的SECRET"}
    
    with open(file_path, 'rb') as f:
        response = requests.post(url, files={"file": f}, headers=headers)
    cid = response.json()['IpfsHash']
    print(f"IPFS CID: {cid}")
    print(f"访问链接: https://ipfs.io/ipfs/{cid}")

if __name__ == "__main__":
    upload_to_ipfs("test.txt")
