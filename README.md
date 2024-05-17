# Network Device Inventory with Streamlit
This Python script utilizes Streamlit to create a web application for managing network device inventory. It retrieves device information from a YAML file and checks their online status using SSH with Netmiko.

## Features:

- Load device data from a YAML configuration file (network_inventory.yml).
- Display device details like name, IP address, model, username, and password.
- Check device online status via SSH.
- User-friendly web interface built with Streamlit.
- Requirements: Python 3, Streamlit, PyYAML, Netmiko

## Instructions:

Install required libraries: pip install streamlit pyyaml netmiko (see requirements file)
Configure your network devices in the network_inventory.yml file. (See example format below)
Run the script: `streamlit run network_inventory.py`
Access the web app in your browser at http://localhost:8501/

Example network_inventory.yml:

````
devices:
  - name: IOS XE on Cat8kv AlwaysOn
    ip_address: 131.226.217.181
    model: IOS XE
    username: [update]
    password: [update]
  - name: Open NX-OS Programmability AlwaysOn
    ip_address: 131.226.217.151
    model: NX-OS
    username: [update]
    password: [update]
  - name: IOS XR Programmabilty AlwaysOn
    ip_address: 131.226.217.150
    model: IOS XR
    username: [update]
    password: [update]

````

The script leverages Streamlit to build the web application's user interface. It displays the loaded device information and utilizes Netmiko to attempt SSH connections to determine the online status of each device.

## Further Enhancements:

Implement functionalities to edit or add devices directly through the web app.
Integrate with network automation tools for configuration management.
This script provides a basic framework for managing network device inventory with a user-friendly web interface. Feel free to customize and extend it based on your specific needs.
