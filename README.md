# survival_with_Cox_model
Survival time calculations with Cox - Weibull and Exponential distributions

'''
Model Assumptions:
* The Cox proportional hazards model assumes that the hazard function for each individual is a constant multiple of a baseline hazard function, with the proportional hazards assumption.
* The model does not specify the form of the baseline hazard function, allowing for flexible modeling of the hazard rate over time.
* It assumes that the effects of covariates on the hazard rate are proportional over time, meaning that the hazard ratio remains constant.


The Cox proportional hazards model is typically specified using the following equation:

_h_(t|X) = _h_0(t) . exp(β1x1 + β2x2 + ... + βpxp)


'''

