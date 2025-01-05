import requests
from get_link import *

def get_page(link):
    
    response = requests.get(link)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the HTML content to a file
        with open("webpage.html", "w", encoding="utf-8") as file:
            file.write(response.text)
        print("Webpage saved as 'webpage.html'")
    else:
        print("Failed to fetch the page. Status code:", response.status_code)

def main():
    x = Date('05', '07', '2000')
    y = Date('05', '07', '2000')
    link = get_link(x,y)

    get_page(link)

if __name__ == '__main__':
    main()