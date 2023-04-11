# Import the os, time, and datetime modules
import os
import time
import datetime

# Define the path to the hosts file
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# Define the redirect IP address
redirect = "127.0.0.1"

# Define the list of websites to block
website_list = ["www.facebook.com", "facebook.com", "www.twitter.com", "twitter.com", "www.instagram.com", "instagram.com"]

# Define the start and end hours of blocking
start_hour = 9
end_hour = 17

# Create an infinite loop that runs every 5 seconds
while True:
    # Get the current time and hour
    current_time = datetime.datetime.now()
    current_hour = current_time.hour

    # Check if the current hour is within the blocking hours
    if start_hour <= current_hour < end_hour:
        # Open the hosts file in append mode
        with open(hosts_path, "a") as file:
            # Loop through the website list
            for website in website_list:
                # Write the redirect IP and the website to the hosts file
                file.write(redirect + " " + website + "\n")
        # Print a message to indicate blocking
        print("Blocked websites")
    else:
        # Open the hosts file in read mode
        with open(hosts_path, "r") as file:
            # Read the lines of the hosts file
            lines = file.readlines()
        # Open the hosts file in write mode
        with open(hosts_path, "w") as file:
            # Loop through the lines of the hosts file
            for line in lines:
                # Check if any website from the list is in the line
                if not any(website in line for website in website_list):
                    # Write the line to the hosts file
                    file.write(line)
        # Print a message to indicate unblocking
        print("Unblocked websites")
    # Wait for 5 seconds before repeating the loop
    time.sleep(5)
