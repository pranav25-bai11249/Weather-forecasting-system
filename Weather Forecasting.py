import pandas as pd
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

start = datetime(2023, 1, 1)

dates = [start + timedelta(days=i) for i in range(365)]

day_num = [i + 1 for i in range(365)]

month = [d.month for d in dates]

temp = [15 + 10 * ((m - 1) / 11) + (i % 7) for i, m in zip(day_num, month)]

humidity = [80 - 0.05 * t + (i % 5) for i, t in zip(day_num, temp)]

data = pd.DataFrame({
    'day':      day_num,
    'month':    month,
    'humidity': humidity,
    'temp':     temp
})

print("=== Sample Weather Data (First 5 Rows) ===")
print(data.head())

X = data[['day', 'month', 'humidity']]

y = data['temp']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nTraining samples: {len(X_train)}, Testing samples: {len(X_test)}")

model = LinearRegression()

model.fit(X_train, y_train)

print("\n=== Model Trained Successfully ===")

pred = model.predict(X_test)

error = mean_absolute_error(y_test, pred)

print(f"Mean Absolute Error (MAE): {error:.2f} °C")
print("(Lower MAE = more accurate predictions)")

future_date = datetime(2024, 7, 15)

future_day    = (future_date - start).days + 1
future_month  = future_date.month
future_humid  = 60

future_input = pd.DataFrame({
    'day':      [future_day],
    'month':    [future_month],
    'humidity': [future_humid]
})

future_temp = model.predict(future_input)

print("\n=== Future Weather Prediction ===")
print(f"Date        : {future_date.strftime('%B %d, %Y')}")
print(f"Humidity    : {future_humid}%")
print(f"Predicted Temperature: {future_temp[0]:.2f} °C")