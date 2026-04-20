import requests
from bs4 import BeautifulSoup


def decode_secret_message(url):
    # Fetch the document content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data from the table rows
    data = []
    # Skip the header row (index 0)
    rows = soup.find_all('tr')[1:]

    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 3:
            try:
                # Based on the doc format: x-coord, char, y-coord
                x = int(cols[0].get_text().strip())
                char = cols[1].get_text().strip()
                y = int(cols[2].get_text().strip())
                data.append((x, y, char))
            except ValueError:
                continue

    if not data:
        print("No valid data found")
        return

    # Determine grid dimensions
    max_x = max(x for x, y, c in data)
    max_y = max(y for x, y, c in data)

    # Initialize grid with spaces
    # Note: y-coordinates usually increase downward in these tasks
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Populate the grid
    for x, y, char in data:
        grid[y][x] = char

    # Print the grid (printing row by row)
    # If the message looks upside down, use reversed(grid)
    for row in reversed(grid):
        print("".join(row))


# Run the function
url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
decode_secret_message(url)