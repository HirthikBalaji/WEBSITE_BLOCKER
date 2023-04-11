# Website Blocker

This project is a website blocker that can block certain websites during certain hours of the day. For example, the user can block social media sites during work hours to avoid distractions. The project uses Python's built-in modules such as time and datetime to check the current time and modify the hosts file to block or unblock websites.

## Features

- Block or unblock websites based on the current hour
- Customize the list of websites to block
- Customize the start and end hours of blocking
- Run the script in the background

## Requirements

- Python 3.6 or higher
- Windows operating system
- Administrator privileges

## Installation

- Clone this repository or download the zip file
- Navigate to the project folder in the command prompt
- Run the script as administrator:

```bash
python website_blocker.py
```

## Usage
- Edit the website_list variable in the script to add or modify the websites to block
- Edit the start_hour and end_hour variables in the script to change the blocking hours
- The script will run in an infinite loop and check the current time every 5 seconds
- The script will modify the hosts file to redirect the blocked websites to localhost
- The script will print a message to indicate blocking or unblocking
