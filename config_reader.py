import xml.etree.ElementTree as ET

def read_config(config_path):
    tree = ET.parse(config_path)
    root = tree.getroot()
    user_name = root.find('username').text
    computer_name = root.find('computername').text
    zip_path = root.find('zip_path').text
    script_path = root.find('script_path').text
    return user_name, computer_name, zip_path, script_path
