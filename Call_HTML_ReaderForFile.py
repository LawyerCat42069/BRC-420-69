import sys
from bs4 import BeautifulSoup

def read_html_file(file_path):
    # Read the HTML file
    with open(file_path, 'r') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract and print the text content
    text_content = soup.get_text()
    print(text_content)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        read_html_file(file_path)
    else:
        print("Usage: python html_reader.py <file_path>")
