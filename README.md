# Weather Forecasting AI

A simple machine learning project that predicts temperature based on day, month, and humidity. Built using Python with just three libraries — pandas, scikit-learn, and datetime.

---

## What This Project Does

It simulates one year of historical weather data, trains a Linear Regression model on it, and then predicts the temperature for any future date you give it. Think of it as a mini version of what weather apps do — but much simpler and completely transparent.

---

## Setup Instructions

Make sure you have Python 3 installed. Then install the required libraries by running:

```
pip install pandas scikit-learn
```

> Note: `datetime` comes built into Python — no installation needed.

---

## How to Run It

1. Download or copy the file `weather_forecast.py` to your computer
2. Open your terminal or command prompt
3. Navigate to the folder where the file is saved
4. Run this command:

```
python weather_forecast.py
```

The program will train the model and print a temperature prediction for July 15, 2024.

---

## What You'll See

- A preview of the generated weather dataset
- Training and testing sample count
- Model accuracy (Mean Absolute Error)
- Predicted temperature for a future date

---

## Want to Change the Prediction Date?

Open `weather_forecast.py` and find this line near the bottom:

```python
future_date = datetime(2024, 7, 15)
```

Change the date to whatever you like and run the file again!
