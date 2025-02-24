import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of website to scrape from
url = 'https://books.toscrape.com/catalogue/category/books/fiction_10/index.html'

book_titles = []
book_prices = []
book_availabilities = []
book_ratings = []

while url:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        books = soup.find_all('article', class_='product_pod')

        for book in books:
            title = book.h3.a['title']
            book_titles.append(title)

            price = book.find('p', class_='price_color').text.strip()
            book_prices.append(price)

            availability = book.find('p', class_='instock availability').text.strip()
            book_availabilities.append(availability)

            # Extract rating
            rating_element = book.find('p', class_='star-rating')
            if rating_element:
                rating_class = rating_element['class'][1].lower() 
                book_ratings.append(rating_class)
            else:
                book_ratings.append(None)  # Handle cases where rating is not found

        next_button = soup.find('li', class_='next')
        if next_button:
            next_url = next_button.a['href']
            url = 'http://books.toscrape.com/catalogue/' + next_url
        else:
            url = None
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)
        break

data = {
    'Title': book_titles,
    'Price': book_prices,
    'Availability': book_availabilities,
    'Rating': book_ratings
}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('books.csv', index=False)
print('Data successfully extracted and saved to books.csv')