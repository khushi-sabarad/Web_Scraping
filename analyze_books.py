import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def load_data(filepath):
    """Loads data from a CSV file."""
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None

def clean_and_prepare_data(df):
    """Cleans and prepares the data for analysis."""
    if df is None:
        return None

    # Clean and convert price to numeric
    df['Price'] = df['Price'].str.replace('£', '').astype(float)

    # Convert 'Rating' to categorical with ordered categories
    df['Rating'] = pd.Categorical(df['Rating'], categories=['one', 'two', 'three', 'four', 'five'], ordered=True)

    return df

def analyze_ratings_distribution(df):
    """Analyzes and visualizes the distribution of book ratings."""
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Rating', data=df)
    plt.title("Distribution of Book Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Number of Books")
    plt.show()

def analyze_average_price_by_rating(df):
    """Calculates and prints the average price by rating."""
    average_price_by_rating = df.groupby('Rating')['Price'].mean().sort_values()
    print("\nAverage Price by Rating:\n", average_price_by_rating)

def find_extreme_prices(df):
    """Prints the top 5 most expensive and cheapest books."""
    print("\nTop 5 Most Expensive Books:")
    for index, row in df.nlargest(5, 'Price')[['Title', 'Price']].iterrows():
        print(f"{row['Title']}: £{row['Price']:.2f}")

    print("\nTop 5 Cheapest Books:")
    for index, row in df.nsmallest(5, 'Price')[['Title', 'Price']].iterrows():
        print(f"{row['Title']}: £{row['Price']:.2f}")

def generate_word_cloud(df):
    """Generates and displays a word cloud of book titles."""
    titles_string = ' '.join(df['Title'].tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles_string)
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def main():
    """Main function to orchestrate the analysis."""
    filepath = 'books.csv'
    df = load_data(filepath)

    if df is not None:
        df = clean_and_prepare_data(df)
        if df is not None:
            print(df.head())
            print(df.info())
            print(df.describe(include='all'))

            analyze_ratings_distribution(df)
            analyze_average_price_by_rating(df)
            find_extreme_prices(df)
            generate_word_cloud(df)

if __name__ == "__main__":
    main()