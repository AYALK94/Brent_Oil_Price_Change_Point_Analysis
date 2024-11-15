import ruptures as rpt

def detect_change_points(data, model="l2", pen=10):
    """Detect change points in the time series data."""
    algo = rpt.Pelt(model=model).fit(data['Price'].values)
    change_points = algo.predict(pen=pen)
    return change_points

if __name__ == "__main__":
    from data_loader import load_data
    import matplotlib.pyplot as plt

    data = load_data('/home/ayalk94/Documents/GitHub/Brent_Oil_Price_Change_Point_Analysis/Data/BrentOilPrices.csv')
    change_points = detect_change_points(data)

    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data['Price'], label='Brent Oil Price')
    for cp in change_points:
        plt.axvline(x=data.index[cp-1], color='red', linestyle='--')
    plt.title('Change Points in Brent Oil Prices')
    plt.show()
