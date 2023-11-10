from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import deque
import pickle
from urllib.parse import urlparse, urljoin

# Start a new session
driver = webdriver.Chrome()

# Base URL
base_url = 'https://xcytedigital.com/'

def pickle_urls(filename, urls):
    # Convert deque to list before pickling
    urls_as_list = list(urls)

    with open(filename, 'wb') as file:
        pickle.dump(urls_as_list, file)

def unpickle_urls(filename):
    with open(filename, 'rb') as file:
        # Load the list from the pickle file
        urls_as_list = pickle.load(file)

        # Convert the list back to a deque
        urls = deque(urls_as_list)

    return urls

# A deque for BFS, and a visited set
urls = deque([base_url])
visited = set()

while urls:
    # Dequeue a URL
    curr_url = urls.popleft()

    # Visit the URL
    driver.get(curr_url)

    # Find all links on the page
    links = driver.find_elements(by=By.TAG_NAME, value='a')

    # Add new links to the deque
    for link in links:
        new_url = link.get_attribute('href')

        # Make sure the new URL is a subpage of the base URL and has not been visited
        if new_url and new_url.startswith(base_url) and new_url not in visited:
            urls.append(new_url)
            visited.add(new_url)

    # Print the URL
    print(curr_url)

# Save the collected URLs to a pickle file
pickle_urls("sublinks.pkl", visited)

# End the session
driver.quit()
