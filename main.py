from random import randint
from time import sleep
from sys import stderr
import os

from pyfiglet import Figlet
from loguru import logger
from web3 import Web3

import config
from data.contract_abi import CONTRACT_ABI

logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <white>{message}</white>")

f = Figlet(font='5lineoblique')
print(f.renderText('Busher'))
print('Telegram channel: @CryptoKiddiesClub')
print('Telegram chat: @CryptoKiddiesChat')
print('Twitter: @CryptoBusher\n')

w3 = Web3(Web3.HTTPProvider(config.RPC))
contract = w3.eth.contract(w3.to_checksum_address(config.CONTRACT_ADDRESS), abi=CONTRACT_ABI)


def set_env_proxy(_proxy):
    os.environ['HTTP_PROXY'] = _proxy
    os.environ['HTTPS_PROXY'] = _proxy


def clear_env_proxy():
    try:
        del os.environ['HTTP_PROXY']
    except KeyError:
        pass
    try:
        del os.environ['HTTPS_PROXY']
    except KeyError:
        pass


def get_claimable_amount(_address, _proxy=None) -> int:
    if proxy:
        set_env_proxy(_proxy)

    claimable_amount_wei = contract.functions.claimableTokens(_address).call()
    _claimable_amount = w3.from_wei(claimable_amount_wei, "ether")

    if proxy:
        clear_env_proxy()

    return _claimable_amount


if __name__ == "__main__":
    with open("wallet_addresses.txt", "r") as file:
        wallet_addresses = [line.strip() for line in file]

    with open("proxies.txt", "r") as file:
        proxies = [line.strip() for line in file]

    for i, address in enumerate(wallet_addresses):
        try:
            proxy = proxies[i]
        except IndexError:
            proxy = None

        try:
            claimable_amount = get_claimable_amount(address, proxy)
            if claimable_amount > 0:
                logger.success(f"{i+1}:{address} - claimable amount: {claimable_amount}")
            else:
                logger.info(f"{i+1}:{address} - claimable amount: {claimable_amount}")
        except Exception as e:
            logger.error(f"{i+1}:{address} - failed to check claimable amount: {e}")

        sleep(randint(config.MIN_DELAY_SEC, config.MAX_DELAY_SEC))
