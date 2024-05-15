import os

PROFILE_FILE = os.path.expanduser("~/.cosmos_rewards_profile")


def read_profile_variable(var_name):
    if os.path.isfile(PROFILE_FILE):
        with open(PROFILE_FILE, 'r') as f:
            for line in f:
                if line.startswith(f"{var_name}="):
                    return line.split('=')[1].strip()
    return None


def write_profile_variable(var_name, var_value):
    lines = []
    if os.path.isfile(PROFILE_FILE):
        with open(PROFILE_FILE, 'r') as f:
            lines = f.readlines()

    with open(PROFILE_FILE, 'w') as f:
        var_written = False
        for line in lines:
            if line.startswith(f"{var_name}="):
                f.write(f"{var_name}={var_value}\n")
                var_written = True
            else:
                f.write(line)
        if not var_written:
            f.write(f"{var_name}={var_value}\n")


def collect_information():
    if not os.path.isfile(PROFILE_FILE):
        open(PROFILE_FILE, 'w').close()

    profile_data = {}
    with open(PROFILE_FILE, 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            profile_data[key] = value

    if profile_data:
        print("Saved information:")
        for key, value in profile_data.items():
            print(f"{key}: {value}")

        use_saved_info = input("Use saved information? (y/n): ").strip().lower()
        if use_saved_info == 'y':
            return

    profile_data['NETWORK_NAME'] = input("Network name: ").strip()
    profile_data['VALIDATOR_ADDRESS'] = input("Validator address: ").strip()
    profile_data['VALIDATOR_WALLET_ADDRESS'] = input("Validator wallet address: ").strip()
    profile_data['BINARY_NAME'] = input("Binary name: ").strip()
    profile_data['TOKEN_DENOM'] = input("Token denomination: ").strip()
    profile_data['WALLET_NAME'] = input("Wallet name: ").strip()
    profile_data['COMMISSION_AMOUNT'] = input("Commission amount: ").strip()

    with open(PROFILE_FILE, 'w') as f:
        for key, value in profile_data.items():
            f.write(f"{key}={value}\n")


def edit_information():
    if not os.path.isfile(PROFILE_FILE):
        print("No profile information found.")
        return

    profile_data = {}
    with open(PROFILE_FILE, 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            profile_data[key] = value

    while True:
        print("Saved information:")
        for key, value in profile_data.items():
            print(f"{key}: {value}")

        print("------ Edit Information ------")
        print("1. Edit network name")
        print("2. Edit validator address")
        print("3. Edit validator wallet address")
        print("4. Edit binary name")
        print("5. Edit token denomination")
        print("6. Edit wallet name")
        print("7. Edit commission amount")
        print("8. Exit")

        edit_option = input("Select an option: ").strip()
        if edit_option == '8':
            break

        if edit_option == '1':
            profile_data['NETWORK_NAME'] = input("Enter new network name: ").strip()
        elif edit_option == '2':
            profile_data['VALIDATOR_ADDRESS'] = input("Enter new validator address: ").strip()
        elif edit_option == '3':
            profile_data['VALIDATOR_WALLET_ADDRESS'] = input("Enter new validator wallet address: ").strip()
        elif edit_option == '4':
            profile_data['BINARY_NAME'] = input("Enter new binary name: ").strip()
        elif edit_option == '5':
            profile_data['TOKEN_DENOM'] = input("Enter new token denomination: ").strip()
        elif edit_option == '6':
            profile_data['WALLET_NAME'] = input("Enter new wallet name: ").strip()
        elif edit_option == '7':
            profile_data['COMMISSION_AMOUNT'] = input("Enter new commission amount: ").strip()
        else:
            print("Error: Invalid option.")

        with open(PROFILE_FILE, 'w') as f:
            for key, value in profile_data.items():
                f.write(f"{key}={value}\n")
        print("Information updated successfully.")
