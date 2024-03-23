# Implementing COX Proportional Hazard Model (for survival) from scratch using scipy's minimize optimization.

import numpy as np
from scipy.optimize import minimize


class CoxPHModel:
    def __init__(self) -> None:
        self.coef_ = None

    def _negative_log_likelihood(self, beta, X, T, E):
        # Compute hazard function
        hazard = np.exp(np.dot(X, beta))
        print(f'training hazard: {hazard}')

        # Compute log likelihood
        ll = np.sum((E * np.log(hazard)) - (T * hazard))

        # Return negative log likelihood
        return ll

    def fit(self, X, T, E):
        # Initialize coefficients
        self.coef_ = np.zeros(X.shape[1])

        # Minimize negative log likelihood using scipy.optimize.minimize
        result = minimize(self._negative_log_likelihood, self.coef_, args=(X, T, E), method='BFGS')

        # Store coefficients
        self.coef_ = result.x

    def predict_churn_time(self, X, threshold=0.5):
        # Compute hazard function using model coefficients
        hazard = np.dot(X, self.coef_)
        print(f'hazard: {hazard}')

        # Calculate time of churn based on survival probabilities
        churn_time = np.log(1 / threshold) / hazard

        return churn_time


# Generate synthetic data
np.random.seed(0)
X_train = np.random.randn(100, 3)

T_train = np.random.randint(1, 50, 100)  # Observed times (durations)
E_train = np.random.choice([0, 1], 100)  # Event indicators (0 if censored, 1 if event occurred)

# Instantiate CoxPH model
model = CoxPHModel()

# Fit model to data
model.fit(X_train, T_train, E_train)

# Predict churn time for new data
X_new = np.random.randn(10, 3)  # Covariates/features of new observations
churn_time = model.predict_churn_time(X_new)

print("Predicted churn times:", churn_time)
