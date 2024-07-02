import subprocess
from cosmos_rewards.profile.profile import read_profile_variable, write_profile_variable


def check_validator_balance():
    binary_name = read_profile_variable("BINARY_NAME")
    wallet_address = read_profile_variable("VALIDATOR_WALLET_ADDRESS")
    token_denom = read_profile_variable("TOKEN_DENOM")

    balance_command = f"{binary_name} query bank balances {wallet_address} --output json | jq -r '.balances[] | select(.denom==\"{token_denom}\") | .amount'"
    balance = subprocess.check_output(balance_command, shell=True).decode().strip()
    print(f"Validator wallet balance ({wallet_address}): {balance} {token_denom}")

def claim_rewards():
    binary_name = read_profile_variable("BINARY_NAME")
    validator_address = read_profile_variable("VALIDATOR_ADDRESS")
    wallet_name = read_profile_variable("WALLET_NAME")
    network_name = read_profile_variable("NETWORK_NAME")
    commission_amount = read_profile_variable("COMMISSION_AMOUNT")
    token_denom = read_profile_variable("TOKEN_DENOM")

    claim_command = f"{binary_name} tx distribution withdraw-rewards {validator_address} --from {wallet_name} --commission --chain-id {network_name} --gas 400000 --fees {commission_amount}{token_denom} --yes"
    subprocess.run(claim_command, shell=True)
    print("Rewards claimed successfully.")


def send_rewards():
    binary_name = read_profile_variable("BINARY_NAME")
    wallet_name = read_profile_variable("WALLET_NAME")
    network_name = read_profile_variable("NETWORK_NAME")
    commission_amount = read_profile_variable("COMMISSION_AMOUNT")
    token_denom = read_profile_variable("TOKEN_DENOM")

    # Check if receiver address is saved
    receiver_address = read_profile_variable("RECEIVER_ADDRESS")

    if receiver_address:
        use_saved_address = input(
            f"Use the saved recipient address ({receiver_address})? (y/n): ").strip().lower()
    else:
        use_saved_address = 'n'

    if use_saved_address != 'y':
        receiver_address = input("Enter the recipient address: ").strip()
        save_address = input("Save the new recipient address? (y/n): ").strip().lower()
        if save_address == 'y':
            write_profile_variable("RECEIVER_ADDRESS", receiver_address)

    # Ask for the amount to send
    amount = input(f"Enter the number of coins to send ({token_denom}): ").strip()

    send_command = f"{binary_name} tx bank send {wallet_name} {receiver_address} {amount}{token_denom} --from {wallet_name} --chain-id {network_name} --gas 400000 --fees {commission_amount}{token_denom} --yes"
    subprocess.run(send_command, shell=True)
    print("Rewards sent successfully.")