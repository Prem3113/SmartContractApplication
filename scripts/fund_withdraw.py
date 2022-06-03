from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund_me():
    fund = FundMe[-1]
    account = get_account()
    entrance_fee = fund.getEntranceFee()
    print(entrance_fee)
    print(f"the current entry fee is {entrance_fee}")
    fund.fund({"from": account, "value": entrance_fee})


def with_draw():
    fund = FundMe[-1]
    account = get_account()
    fund.withdraw({"from": account})


def main():
    fund_me()
    with_draw()
