import sys
import requests
from bs4 import BeautifulSoup

def strip_html_tags(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python anti_html.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        cleaned_html = strip_html_tags(response.text)

        print(cleaned_html)

    except requests.RequestException as e:
        print(f"Error: Failed to fetch URL - {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()