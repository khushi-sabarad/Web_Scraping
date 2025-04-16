# Web-Scraped Book Data Analyzer

This project demonstrates web scraping and data analysis using Python to extract and analyze book data from [books.toscrape.com](https://books.toscrape.com/). The goal was to gather information about book prices, ratings, and titles to identify market trends and patterns.

## What is Web Scraping?

Web scraping is the process of automatically extracting data from websites. It involves fetching web pages, parsing their HTML content, and extracting the desired information. This project utilizes web scraping to gather book data for analysis.

## Project Overview

This project consists of two main parts:

1.  **Web Scraping:**
    * Uses `requests` to fetch HTML content from [books.toscrape.com](https://books.toscrape.com/).
    * Employs `Beautiful Soup` to parse the HTML and extract book titles, prices, ratings, and availability.
    * Handles pagination to scrape data from multiple pages.
    * Saves the scraped data to a CSV file (`books.csv`).

2.  **Data Analysis:**
    * Loads the scraped data from the CSV file using `pandas`.
    * Cleans and prepares the data for analysis (e.g., converting prices to numeric, handling ratings as categorical).
    * Performs various analyses, including:
        * Distribution of book ratings.
        * Average price by rating.
        * Finding the most expensive and cheapest books.
        * Generating a word cloud of book titles.
    * Visualizes the distribution of book ratings and generates a word cloud using `matplotlib`, `seaborn`, and `wordcloud`.

## Code Structure

* `web_scraping_books.py`: Contains the web scraping code.
* `analyze_books.py`: Contains the data analysis and visualization code.
* `books.csv`: The CSV file containing the scraped data.

## Libraries Used

* `requests`: For making HTTP requests.
* `Beautiful Soup`: For parsing HTML.
* `pandas`: For data manipulation and analysis.
* `matplotlib`: For data visualization.
* `seaborn`: For enhanced data visualizations.
* `wordcloud`: For generating word clouds.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone [repository URL]
    cd [repository directory]
    ```
2.  **Install dependencies:**
    ```bash
    pip install requests beautifulsoup4 pandas matplotlib seaborn wordcloud
    ```
3.  **Run the web scraping script:**
    ```bash
    python web_scraping_books.py
    ```
    This will create the `books.csv` file.
4.  **Run the data analysis script:**
    ```bash
    python analyze_books.py
    ```
    This will display the analysis results and visualizations.

## Code Explanation

* **`web_scraping_books`:**
    * The `scrape_books(url)` function scrapes book data from a single page.
    * The `scrape_all_pages(base_url)` function iterates through all pages and calls `scrape_books()` for each page.
    * Data is saved to a CSV file.
* **`analyze_books.py`:**
    * The `load_data(filepath)` function loads data from the CSV file.
    * The `clean_and_prepare_data(df)` function cleans the data.
    * The `analyze_ratings_distribution(df)` function creates a countplot of ratings.
    * The `analyze_average_price_by_rating(df)` function calculates the average price by rating.
    * The `find_extreme_prices(df)` function prints the most expensive and cheapest books.
    * The `generate_word_cloud(df)` function creates and displays a word cloud.
    * The `main()` function orchestrates the analysis.

## Potential Improvements

* Implement more robust error handling.
* Add logging for better tracking of the scraping and analysis process.
* Explore more advanced data analysis techniques.
* Integrate with a database for scalable data storage.
* Add a feature to scrape different categories.
