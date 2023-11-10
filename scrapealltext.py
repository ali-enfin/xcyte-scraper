from selenium import webdriver
from selenium.webdriver.common.by import By


# Start a new session
driver = webdriver.Chrome()

# Navigate to the URL
url = 'https://xcytedigital.com/virtual-events/'
driver.get(url)

# Find the HTML element that contains the text
# For example, if you want to get text from the entire body of the HTML document:
body_element = driver.find_elements(by=By.TAG_NAME, value='body')

print(body_element[0])

# Extract text content
text_content = body_element.text

# Print or process the extracted text
print(text_content)

# End the session
driver.quit()
