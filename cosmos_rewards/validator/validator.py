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