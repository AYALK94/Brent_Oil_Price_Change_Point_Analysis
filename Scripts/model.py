from statsmodels.tsa.arima.model import ARIMA
from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np

def train_arima_model(data, order=(5, 1, 0)):
    """Train an ARIMA model."""
    model = ARIMA(data['Price'], order=order)
    model_fit = model.fit()
    return model_fit

def train_lstm_model(data, look_back=60):
    """Train an LSTM model for price prediction."""
    series = data['Price'].values.reshape(-1, 1)
    X, y = [], []
    for i in range(look_back, len(series)):
        X.append(series[i-look_back:i, 0])
        y.append(series[i, 0])
    X, y = np.array(X), np.array(y)
    X = X.reshape((X.shape[0], X.shape[1], 1))
    
    model = Sequential([
        LSTM(50, return_sequences=False, input_shape=(look_back, 1)),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X, y, epochs=20, batch_size=32, verbose=2)
    return model

if __name__ == "__main__":
    from data_loader import load_data
    data = load_data('/home/ayalk94/Documents/GitHub/Brent_Oil_Price_Change_Point_Analysis/Data/BrentOilPrices.csv')
    arima_model = train_arima_model(data)
    print(arima_model.summary())
