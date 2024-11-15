import pandas as pd

def load_data(file_path):
    """Load and preprocess Brent oil prices data."""
    df = pd.read_csv(file_path, parse_dates=['Date'], dayfirst=True)
    df.sort_values('Date', inplace=True)
    df.set_index('Date', inplace=True)
    return df

if __name__ == "__main__":
    data = load_data('/home/ayalk94/Documents/GitHub/Brent_Oil_Price_Change_Point_Analysis/Data/BrentOilPrices.csv')
    print(data.head())
