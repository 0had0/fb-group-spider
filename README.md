# Facebook Group Post Scraper using Selenium

The **Facebook Group Post Scraper** is a Python script designed to help you scrape posts from a given list of Facebook groups using Selenium. This script allows you to extract valuable information and data from various Facebook groups, which can be useful for analysis, research, or any other purposes.

## Prerequisites

Before running the script, ensure you have the following dependencies installed:

- Python 3.x
- Selenium library
- Chrome WebDriver (or any other browser's WebDriver of your choice)

You can install the Selenium library using `pip`:

```bash
pip install selenium
```

Make sure to download the Chrome WebDriver and place it in a location that is included in your system's PATH.

## Usage

Follow these steps to run the script and scrape posts from your desired Facebook groups:

1. Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/your-username/facebook-group-post-scraper.git
cd facebook-group-post-scraper
```

2. Open the `config.py` file and add the list of Facebook groups you want to scrape:

```python
# Add the URLs of Facebook groups you want to scrape along with your facebook email and password (use a fake acount with no 2fa)
groups = [
    "https://www.facebook.com/groups/group1",
    "https://www.facebook.com/groups/group2",
    "https://www.facebook.com/groups/group3",
    # Add more group URLs as needed
]
email = "<you-email>"
password="<password>"
```

3. Run the script:

```bash
python scraper.py
```

4. The script will start scraping posts from the specified Facebook groups using Selenium. The extracted data will be saved to a `posts.json` file for further analysis.

## Output

The script will create a `posts.json` file in the project directory, which will contain the scraped data in JSON format. The JSON file will include the following information for each post:

[ ] Post ID
[ ] Group Name
[X] Post Text
[ ] Post URL
[ ] Post Time
[ ] Images links

## TODO

[ ] Implement a function to handle login to Facebook to access private groups if needed (make login optional).
[ ] Add error handling for possible exceptions during scraping to ensure the script continues running smoothly.
[ ] Add command-line options.
[ ] Consider implementing rate limiting to avoid excessive requests to Facebook servers and prevent potential bans.
[ ] Add an option to export data to CSV or other formats for compatibility with various data analysis tools.
[ ] Use multithreading.
[ ] Add better logging functionality to keep track of scraping progress and any potential issues encountered.

## Note

- Ensure you have proper access permissions to scrape posts from the Facebook groups you want to target. Respect the terms of service of Facebook and the rules of the groups you are scraping.

- The script is for educational and personal use only. Use it responsibly and avoid any actions that might violate the privacy or terms of service of Facebook or its users.

Happy scraping! 🕷️
