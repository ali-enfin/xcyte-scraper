from collections import deque
import pickle

def unpickle_urls(filename):
    with open(filename, 'rb') as file:
        # Load the list from the pickle file
        urls_as_list = pickle.load(file)
        filtered_list = [element for element in urls_as_list if "#" not in element]
        # Convert the list back to a deque
        urls = deque(urls_as_list)

    return filtered_list

print(unpickle_urls('./sublinks.pkl'))

