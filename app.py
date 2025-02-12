import streamlit as st
import datetime
import requests
from pathlib import Path

# Function to log IP addresses
def log_ip():
    # Fetch the IP address from an external API
    response = requests.get('https://api.ipify.org?format=json')
    visitor_ip = response.json()['ip']  # Get the visitor's IP
    visit_time = datetime.datetime.now()  # Get the current time
    with open("ip_log.txt", "a") as file:
        file.write(f"IP: {visitor_ip} at {visit_time}\n")
    return visitor_ip

# Read the HTML content from the file
def load_html():
    html_file = Path("html.html")
    if html_file.exists():
        with open(html_file, "r") as file:
            return file.read()
    else:
        return "<h1>HTML file not found!</h1>"

# Create the main layout
st.title("Website Logging App")

# Log the visitor's IP address
visitor_ip = log_ip()

# Display the IP address and load the HTML content
st.write(f"Visitor IP: {visitor_ip}")
st.markdown(load_html(), unsafe_allow_html=True)
