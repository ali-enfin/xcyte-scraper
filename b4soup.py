import requests                                                                                                                                   
from bs4 import BeautifulSoup                                                                                                                     
                                                                                                                                                    
# URL of the website to be scraped                                                                                                                
url = 'https://xcytedigital.com/'                                                                                                                 
                                                                                                                                                    
# Send a GET request to the website                                                                                                               
response = requests.get(url)                                                                                                                      
                                                                                                                                                    
# Make sure we got a valid response                                                                                                               
if not response.ok:                                                                                                                               
    # If the response was not ok, print the HTTP status code and exit                                                                             
    print('Error', response.status_code)                                                                                                          
    exit()                                                                                                                                        
                                                                                                                                                    
# Get the full HTML content
print(response.content)
print(response.text)                                                                                                                       
page_content = response.text                                                                                                                      
                                                                                                                                                    
# Parse the page content with BeautifulSoup                                                                                                       
soup = BeautifulSoup(response.content, 'html.parser')                                                                                                 
                                                                                                                                                    
# Extract all text from the parsed HTML                                                                                                           
text_only = soup.get_text()                                                                                                                       
                                                                                                                                                    
# Define the filename for the TXT file                                                                                                            
filename = './website_content.txt'                                                                                                                
                                                                                                                                                    
# Open the file in write mode                                                                                                                     
with open(filename, 'w') as file:                                                                                                                 
    # Write the text to the file                                                                                                                  
    file.write(text_only)                                                                                                                         
                                                                                                                                                    
print(f'Successfully wrote scraped content to {filename}!')  