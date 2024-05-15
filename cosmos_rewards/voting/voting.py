import subprocess
import requests
from cosmos_rewards.profile.profile import read_profile_variable, write_profile_variable


def check_active_votings():
    api_address = read_profile_variable("API_ADDRESS")
    if not api_address:
        api_address = input("Enter API address: ")
        write_profile_variable("API_ADDRESS", api_address)

    for api_version in ['v1beta1', 'v1']:
        response = requests.get(f"{api_address}/cosmos/gov/{api_version}/proposals?pagination.limit=800")
        if response.status_code != 200:
            continue

        proposals = response.json().get('proposals', [])
        for proposal in proposals:
            if proposal.get('status') == "PROPOSAL_STATUS_VOTING_PERIOD":
                print(f"Voting ID: {proposal.get('id')}")
                print(f"Description: {proposal['content'].get('title')}")
                print(f"Voting End Time: {proposal.get('voting_end_time')}")
                print("----------------------")


def perform_voting():
    binary_name = read_profile_variable("BINARY_NAME")
    wallet_name = read_profile_variable("WALLET_NAME")
    network_name = read_profile_variable("NETWORK_NAME")
    commission_amount = read_profile_variable("COMMISSION_AMOUNT")
    token_denom = read_profile_variable("TOKEN_DENOM")

    proposal_id = input("Enter the proposal ID to vote: ")
    vote_option = input("Enter your vote (yes/no): ")

    voting_command = f"{binary_name} tx gov vote {proposal_id} {vote_option} --from {wallet_name} --chain-id {network_name} --fees {commission_amount}{token_denom} --yes"
    subprocess.run(voting_command, shell=True)
    print("Voting submitted successfully.")