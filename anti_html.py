import sys
import requests
from bs4 import BeautifulSoup  # Assuming you have BeautifulSoup installed

def strip_html_tags(html):
    # Parse HTML using BeautifulSoup and extract text
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    return text

def main():
    # Check if URL is provided as command-line argument
    if len(sys.argv) != 2:
        print("Usage: python anti_html.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        # Send GET request to URL and retrieve HTML content
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Strip HTML tags from the HTML content
        cleaned_html = strip_html_tags(response.text)

        # Print the cleaned HTML content
        print(cleaned_html)

    except requests.RequestException as e:
        print(f"Error: Failed to fetch URL - {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()