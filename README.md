# Cookie Clicker Automation Script

This script uses Selenium and Python to automate the cookie-clicking game located at orteil.dashnet.org/experiments/cookie/.

## Requirements

- Selenium
- ChromeDriver
- Usage

Clone the repository
Install the required packages using `pip install -r requirements.txt`.
Download ChromeDriver and add its path to the `chrome_driver_path` variable in the script
Run the script using python main.py

## Details

The script uses Selenium to open a ChromeDriver session and navigate to the cookie-clicking game. It then finds the cookie element on the page and clicks it using a loop. After 5 minutes, the script prints the number of cookies per second (cps) and exits. Additionally, the script checks the store every 5 seconds and buys the last item that can be bought (that is not grayed out).

## Note

The code is written to work with a specific version of the cookie-clicking game and may not work with future versions of the game.