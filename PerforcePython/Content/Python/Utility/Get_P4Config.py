"""
Gets values from Unreal's source control ini file.

Execute Python Script Node:
Inputs: 
- source_control_ini_path: str

Outputs:
- server: str
- username: str
- workspace: str
- error_message: str
"""

import configparser
import os

print("p4config being called")

error_message = ""


def parse_ini(file_path):
    if not os.path.exists(file_path):
        error_message = f"INI file not found: {file_path}"
        raise FileNotFoundError(error_message)

    config = configparser.ConfigParser()
    with open(file_path, "r") as f:
        config.read_file(f)
        f.seek(0)
        config_text = f.read()

    sc_settings = config["SourceControl.SourceControlSettings"]
    if (provider := sc_settings.get("Provider")) != "Perforce":
        error_message = f"Source control provider '{provider}' is not Perforce"
        print(config_text)
        raise ValueError(error_message)

    p4_settings = config["PerforceSourceControl.PerforceSourceControlSettings"]
    if p4_settings.getboolean("UseP4Config"):
        error_message = "This script currently does not work with p4config because of the weird way that Unreal sets the current working directory."
        print(config_text)
        raise ValueError(error_message)

    return {
        "Port": p4_settings["Port"],
        "UserName": p4_settings["UserName"],
        "Workspace": p4_settings["Workspace"],
    }


# ini file path will be passed in from UE blueprints called: source_control_ini_path
settings = parse_ini(source_control_ini_path)
print(settings)
server = settings["Port"]
username = settings["UserName"]
workspace = settings["Workspace"]
