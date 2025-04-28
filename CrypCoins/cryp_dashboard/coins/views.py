from django.shortcuts import render
from datetime import datetime, timedelta
import random
import json

def dashboard(request):
    # Mock data generation
    bitcoin_prices = []
    ethereum_prices = []
    dogecoin_prices = []

    current_date = datetime.today() - timedelta(days=180)  # Start from 6 months ago

    for _ in range(26):  # 26 weekly data points
        bitcoin_prices.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'price': round(34000 + random.uniform(-500, 500), 2)
        })
        ethereum_prices.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'price': round(1800 + random.uniform(-100, 100), 2)
        })
        dogecoin_prices.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'price': round(0.08 + random.uniform(-0.01, 0.01), 4)
        })
        current_date += timedelta(days=7)

    # Structure the result
    result = {
        'Bitcoin': bitcoin_prices,
        'Ethereum': ethereum_prices,
        'Dogecoin': dogecoin_prices
    }

    return render(request, "coins/index.html", {
        'coin_data': json.dumps(result),
        'error_message': None
    })
