import os
import streamlit as st
import yaml
from netmiko import ConnectHandler

# Construct the absolute path to the YAML file
yaml_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'network_inventory.yml')

try:
    if os.path.exists(yaml_file):
        with open(yaml_file, 'r') as file:
            inventory = yaml.safe_load(file)
    else:
        st.error(f"Error: '{yaml_file}' file not found.")
        st.stop()
except PermissionError:
    st.error("Error: Insufficient permissions to read 'network_inventory.yml' file.")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")
    st.stop()

# Define the Streamlit app
st.title("Network Device Inventory")

# Function to check if a device is online via SSH
def check_device_online(device):
    try:
        net_connect = ConnectHandler(
            device_type='cisco_ios',
            ip=device['ip_address'],
            username=device['username'],
            password=device['password'],
            timeout=5
        )
        net_connect.disconnect()
        return True
    except Exception as e:
        return False

# Display the inventory
if 'devices' in inventory:
    st.write("# Devices")
    for device in inventory['devices']:
        st.subheader(device['name'])
        st.write(f"**IP Address:** {device['ip_address']}")
        st.write(f"**Model:** {device['model']}")

        # Check if the device is online via SSH
        if check_device_online(device):
            st.write(f"**Status:** Online")
        else:
            st.write(f"**Status:** Offline")

        st.write(f"**Username:** {device['username']}")
        st.write(f"**Password:** {device['password']}")
        st.write("---")
else:
    st.error("No devices found in the inventory.")
