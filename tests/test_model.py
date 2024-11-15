import pytest
from data_loader import load_data
from model import train_arima_model

def test_arima_model():
    data = load_data('/home/ayalk94/Documents/GitHub/Brent_Oil_Price_Change_Point_Analysis/Data/BrentOilPrices.csv')
    model = train_arima_model(data, order=(1, 1, 1))
    assert model is not None, "ARIMA model training failed"
