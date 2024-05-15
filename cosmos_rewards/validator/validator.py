import subprocess
import os
from cosmos_rewards.profile.profile import read_profile_variable, write_profile_variable


def check_database_weight():
    project_directory = input("Enter the project's working directory: ")
    if not os.path.isdir(project_directory):
        print("Error: The specified directory does not exist.")
        return

    weight = subprocess.check_output(['du', '-sh', project_directory]).split()[0].decode()
    print(f"Database weight of the project directory: {weight} GB")


def update_peers():
    project_directory = read_profile_variable("PROJECT_DIRECTORY")
    if not project_directory:
        project_directory = input("Enter the project directory: ")
        write_profile_variable("PROJECT_DIRECTORY", project_directory)
    if not os.path.isdir(project_directory):
        print("Error: The specified directory does not exist.")
        return

    peers = input("Enter the peers: ")
    config_file = f"{project_directory}/config/config.toml"
    with open(config_file, 'r') as file:
        config = file.read()
    config = config.replace('persistent_peers = ""', f'persistent_peers = "{peers}"')
    with open(config_file, 'w') as file:
        file.write(config)
    print("Peers updated successfully.")


def edit_validator():
    project_directory = read_profile_variable("PROJECT_DIRECTORY")
    if not project_directory:
        project_directory = input("Enter the project directory: ")
        write_profile_variable("PROJECT_DIRECTORY", project_directory)
    if not os.path.isdir(project_directory):
        print("Error: The specified directory does not exist.")
        return

    new_moniker = read_profile_variable("NEW_MONIKER")
    identity = read_profile_variable("IDENTITY")
    details = read_profile_variable("DETAILS")
    website = read_profile_variable("WEBSITE")
    wallet_name = read_profile_variable("WALLET_NAME")
    network_name = read_profile_variable("NETWORK_NAME")
    binary_name = read_profile_variable("BINARY_NAME")
    commission_amount = read_profile_variable("COMMISSION_AMOUNT")
    token_denom = read_profile_variable("TOKEN_DENOM")

    if not new_moniker:
        new_moniker = input("Enter the new moniker name: ")
        write_profile_variable("NEW_MONIKER", new_moniker)
    if not identity:
        identity = input("Enter your Keybase ID: ")
        write_profile_variable("IDENTITY", identity)
    if not details:
        details = input("Enter details about your validator: ")
        write_profile_variable("DETAILS", details)
    if not website:
        website = input("Enter your website URL: ")
        write_profile_variable("WEBSITE", website)
    if not wallet_name:
        wallet_name = input("Enter the key to use for the transaction: ")
        write_profile_variable("WALLET_NAME", wallet_name)
    if not binary_name:
        binary_name = input("Enter the binary name: ")
        write_profile_variable("BINARY_NAME", binary_name)
    if not commission_amount:
        commission_amount = input("Enter the fees amount: ")
        write_profile_variable("COMMISSION_AMOUNT", commission_amount)
    if not token_denom:
        token_denom = input("Enter the token denomination: ")
        write_profile_variable("TOKEN_DENOM", token_denom)
    if not network_name:
        network_name = input("Enter the network name: ")
        write_profile_variable("NETWORK_NAME", network_name)

    edit_command = f"{binary_name} tx staking edit-validator --new-moniker {new_moniker} --identity {identity} --details \"{details}\" --website {website} --chain-id {network_name} --commission-rate 0.05 --from {wallet_name} --fees {commission_amount}{token_denom} --yes"
    subprocess.run(edit_command, shell=True)
    print("Validator updated successfully.")
