import matplotlib.pyplot as plt
import seaborn as sns

def plot_price_trends(data):
    """Visualize Brent oil price trends."""
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data['Price'], label='Brent Oil Price')
    plt.xlabel('Date')
    plt.ylabel('Price (USD per Barrel)')
    plt.title('Brent Oil Price Trend')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    from data_loader import load_data
    data = load_data('/home/ayalk94/Documents/GitHub/Brent_Oil_Price_Change_Point_Analysis/Data/BrentOilPrices.csv')
    plot_price_trends(data)
