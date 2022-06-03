from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fundme
import pytest
from brownie import network, FundMe, accounts, exceptions


def test_can_fund_withdraw():
    account = get_account()
    fund_me = deploy_fundme()
    Entrance_fee = fund_me.getEntranceFee()
    tx1 = fund_me.fund({"from": account, "value": Entrance_fee})
    tx1.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == Entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for testing.....")
    fund_me = deploy_fundme()
    bad_actor = accounts.add()
    # fund_me.withdraw({"from": bad_actor})
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
