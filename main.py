import os
import time
import requests
from bs4 import BeautifulSoup
import json

QUOTES_TOSCRAPE_URL = "https://quotes.toscrape.com/"


def scrape_quotes() -> list:
    """Returns a list of dictionaries with data about quotes, authors and tags"""
    quotes_data = []
    page = 1 # Page number

    while True:
        try:
            # Get the HTML of the current page
            response = requests.get(f"{QUOTES_TOSCRAPE_URL}/page/{page}")
            response.raise_for_status() # Checking if the request was successful

            soup = BeautifulSoup(response.text, "html.parser")
            quotes = soup.find_all("div", class_="quote") # Searching for blocks with quotes on the page

            # If there are no citations on the page, then the end of the page list has been reached
            if not quotes:
                print("Data collection complete: last page reached")
                break
            
            # Process each quote on the page
            for quote in quotes:
                # Get text of the quote
                text = quote.find("span", class_="text").get_text()
                # Get author of the quote
                author = quote.find("small", class_="author").get_text()
                # Get tags (list) of the quote
                tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]
                # Adding quotes to the quotes_data list
                quotes_data.append({
                    "quote": text,
                    "author": author,
                    "tags": tags
                })

            print(f"Page {page} has been processed")
            page += 1
            
            time.sleep(1) # Delay between requests
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to page {page}: {e}")
            break
    
    return quotes_data

            
def save_to_json(data, filepath="data/quotes.json"): 
    """Saving data to JSON file"""
    try:
        # Create a folder if it doesn't exist yet
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # Save data to JSON file
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=3)
        print(f"Data has been saved successfully to {filepath}")
    except IOError as e:
        print(f"Error saving data: {e}")


if __name__ == "__main__":
    try: 
        quotes = scrape_quotes() 
        save_to_json(quotes)
    except Exception as e:
        print(f"Program error: {e}")