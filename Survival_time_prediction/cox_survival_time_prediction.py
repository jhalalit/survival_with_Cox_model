# Import necessary libraries
import pandas as pd
import numpy as np
from lifelines import CoxPHFitter
from lifelines.datasets import load_rossi

# Load example dataset (Rossi recidivism dataset)
data = load_rossi()

# Fit Cox proportional hazards model
cph = CoxPHFitter()
cph.fit(data, duration_col='week', event_col='arrest')

# Predict survival probabilities for each customer
survival_probabilities = cph.predict_survival_function(data)

# Identify churn events based on a threshold (e.g., churn probability > 0.5)
churn_events = survival_probabilities < 0.5

# Find time of churn for each customer
time_of_churn = survival_probabilities.index[churn_events.idxmax()]

# Display time of churn for the first few customers
print(time_of_churn.head())