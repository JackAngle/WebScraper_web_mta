# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os

my_dir = os.path.dirname(__file__)


# Set the URL you want to webscrape from
url = 'http://web.mta.info/developers/turnstile.html'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
line_count = 1  # variable to track what line you are on
for one_a_tag in soup.findAll('a'):  # 'a' tags are for links
    if line_count >= 36: # code for text files starts at line 36
        link = one_a_tag['href']
        download_url = 'http://web.mta.info/developers/' + link
        # Stored location path
        path_to_save = os.path.join(my_dir, link[link.find('/turnstile_')+1:].replace('/', "\\"))
        # Stored location's directory path
        dir_path = path_to_save[:path_to_save.rfind('\\'):]
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print("Directory ", dir_path, " Created ")

        urllib.request.urlretrieve(download_url, path_to_save)
        print(download_url, path_to_save)
        # pause the code for a sec
        time.sleep(1)
    # add 1 for next line
    line_count += 1
