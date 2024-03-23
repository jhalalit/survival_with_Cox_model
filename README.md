# survival_with_Cox_model
Survival time calculations with Cox - Weibull and Exponential distributions

'''
Model Assumptions:
* The Cox proportional hazards model assumes that the hazard function for each individual is a constant multiple of a baseline hazard function, with the proportional hazards assumption.
* The model does not specify the form of the baseline hazard function, allowing for flexible modeling of the hazard rate over time.
* It assumes that the effects of covariates on the hazard rate are proportional over time, meaning that the hazard ratio remains constant.


The Cox proportional hazards model is typically specified using the following equation:

_h_(t|X) = _h0_(t) . exp(_β1_ x1 + _β2_ x2 + ... + _βp_ xp)

Where:
* _h_(t∣x) is the hazard function for an individual with covariate values 
* _h0_(t) is the baseline hazard function, representing the hazard rate for an individual with all covariates set to zero.
β1, β2 etc. are the coefficients (log hazard ratios) associated with the covariates

'''

