# Zostel Vagamon Menu Scraper

## Project Description
This project is a Python-based web scraper that extracts the menu from the Monkey Tribe Cafe at Zostel Vagamon and saves it to an Excel file.  It was created to automate the process of retrieving and updating menu prices, a task that was observed to be done manually and inefficiently at the hostel.

## Background Story
During my time volunteering at Zostel Vagamon for two months, I witnessed the manual process of updating the cafe menu prices.  Whenever there was a change in pricing (such as during peak season), the receptionist would copy and paste the menu items and their prices from the online menu into a text file. This file was then sent to the property manager, who would again manually retype the data, adding the new prices in a bracket after each item.

This repetitive, time-consuming process struck me as a perfect example of a task that could be easily automated with web scraping.  Instead of error-prone manual entry, a simple script could:

1. Fetch the latest menu data directly from the source (the online cafe menu).
2. Generate a clean Excel file.
3. This file could then be used to calculate new prices by applying a percentage increase using Excel functions, significantly reducing the workload and potential for errors.

This project aims to provide a quick and efficient way to get the menu in a structured format, ready for further processing.

## Features
- Web Scraping: Extracts menu data (item names and prices) from the Monkey Tribe Cafe Vagamon website.
- Excel Output: Saves the scraped data into an Excel file (.xlsx) using the pandas library.
- Structured Data: The Excel file is formatted for easy use, with item names and prices in separate columns.
- Error Handling: Includes error handling for web page fetching and file saving.

## Code Explanation
The script is written in Python and uses the following libraries:
- `requests`: For sending HTTP requests to fetch the HTML content of the webpage.
- `BeautifulSoup`: For parsing the HTML content and navigating the document structure to locate the menu data.
- `pandas`: For creating a DataFrame to store the scraped data and saving it to an Excel file.
- `openpyxl`: For advanced manipulation of the Excel file, specifically for formatting the output (making category names bold).

## How the Script Works
1. Fetching the Webpage:
- The script uses the `requests.get()` function to retrieve the HTML content from the Monkey Tribe Cafe Vagamon website.
- It includes error handling using `response.raise_for_status()` to catch any potential issues with the request (e.g., the website is down, or the page is not found).

2. Parsing the HTML:
- The `BeautifulSoup` library is used to parse the HTML content, creating a navigable tree structure.
- The script then uses BeautifulSoup's methods (e.g., `find_all()`, `find())` to locate the specific HTML elements that contain the menu data.  This is done by identifying HTML tags and CSS classes.

3. Locating Menu Data:
- The script targets specific `<span>` tags with the class wixui-rich-text__text.
- It uses the `style` attribute of these tags, specifically the `font-family`, to differentiate between category headings and menu item names/prices.

4. Data Extraction:
The script iterates through the located elements and extracts the relevant text for the category, item name, and price, cleaning the data by removing extra whitespace.

5. Data Structuring:
- The extracted data is organized into a Python dictionary, where the keys are the menu categories (e.g., "Appetizers", "Soups"), and the values are lists of dictionaries, with each dictionary containing the "item" name and "price".
- This structured data is then converted into a pandas DataFrame.

6. Saving to Excel:
- The `pandas` library is used to create a DataFrame and save it to an Excel file (.xlsx) using the to_excel() method.
- The `openpyxl` library is used to further format the excel file (The category rows are made bold).

Open the menu.xlsx file with Microsoft Excel or another spreadsheet program.
- The data will be organized into three columns:
  - Name: Contains the Category name and Item Name.
  - Price: Contains the price of the item.
  - Category: "Category" or "Item" to help with filtering.
- You can then use Excel functions to add a column for the new price (e.g., by applying a percentage increase) as required.

## Disclaimer
* The structure of the website may change. If the script fails, you may need to modify the element selectors in the code.
