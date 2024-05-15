from cosmos_rewards.profile.profile import collect_information, edit_information
from cosmos_rewards.rewards.rewards import check_validator_balance, claim_rewards
from cosmos_rewards.voting.voting import check_active_votings, perform_voting
from cosmos_rewards.validator.validator import check_database_weight, update_peers, edit_validator


def main_menu():
    while True:
        print("-------- Menu --------")
        print("1. Enter network and validator information")
        print("2. Rewards Management")
        print("3. Voting Management")
        print("4. Validator Management")
        print("5. Edit network information")
        print("6. Exit")

        option = input("Select an option: ").strip()
        print("----------------------")

        if option == '1':
            collect_information()
        elif option == '2':
            rewards_menu()
        elif option == '3':
            voting_menu()
        elif option == '4':
            validator_menu()
        elif option == '5':
            edit_information()
        elif option == '6':
            print("Goodbye!")
            break
        else:
            print("Error: Invalid option.")
        print("----------------------")


def rewards_menu():
    while True:
        print("-------- Rewards Management --------")
        print("1. Check validator balance")
        print("2. Claim rewards from validator")
        print("3. Back")

        option = input("Select an option: ").strip()
        print("----------------------")

        if option == '1':
            check_validator_balance()
        elif option == '2':
            claim_rewards()

        elif option == '3':
            break
        else:
            print("Error: Invalid option.")
        print("----------------------")


def voting_menu():
    while True:
        print("-------- Voting Management --------")
        print("1. Check active votings")
        print("2. Perform voting")
        print("3. Back")

        option = input("Select an option: ").strip()
        print("----------------------")

        if option == '1':
            check_active_votings()
        elif option == '2':
            perform_voting()
        elif option == '3':
            break
        else:
            print("Error: Invalid option.")
        print("----------------------")


def validator_menu():
    while True:
        print("-------- Validator Management --------")
        print("1. Check database weight")
        print("2. Update peers")
        print("3. Update validator information")
        print("4. Back")

        option = input("Select an option: ").strip()
        print("----------------------")

        if option == '1':
            check_database_weight()
        elif option == '2':
            update_peers()
        elif option == '3':
            edit_validator()
        elif option == '4':
            break
        else:
            print("Error: Invalid option.")
        print("----------------------")
