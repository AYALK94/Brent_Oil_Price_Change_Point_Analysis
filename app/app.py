# import sys
# import os
# from flask import Flask, render_template

# # Add the root directory to sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# # Now import the data_loader module from Scripts
# from Scripts.data_loader import load_data

# app = Flask(__name__)

# @app.route('/')
# def dashboard():
#     data = load_data('/home/ayalk94/Documents/GitHub/Brent_Oil_Price_Change_Point_Analysis/Data/BrentOilPrices.csv')
#     return render_template('dashboard.html', data=data.to_html())

# if __name__ == "__main__":
#     app.run(debug=True)

# import json







from flask import Flask, render_template
import sys
import os

# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import the data_loader module from Scripts
from Scripts.data_loader import load_data

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Load the data
    data = load_data('/home/ayalk94/Documents/GitHub/Brent_Oil_Price_Change_Point_Analysis/Data/BrentOilPrices.csv')

    # Clean the dates (ensure they're serializable)
    dates = data.index.tolist()
    dates = [str(date) for date in dates if date is not None]  # Convert to string and remove None values

    # Clean the 'prices' or any other column data
    prices = data['Price'].dropna().tolist()  # Ensure no NaN values
    prices = [float(price) for price in prices]  # Ensure all prices are floats

    # Render the template with data, dates, and prices
    return render_template('dashboard.html', data=data.to_html(), dates=dates, prices=prices)

    


# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)
