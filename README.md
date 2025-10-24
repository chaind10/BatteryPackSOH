# Battery SOH Prediction using Linear Regression

## Overview
This project predicts the State of Health (SOH) of a battery pack using Linear Regression and real-world voltage data from the PulseBat Dataset.  

The model uses 21 cell voltages (`U1–U21`) as input features and outputs the pack’s overall health.

If the predicted SOH is below 0.6, the battery is flagged as “Problematic” otherwise we can classify it as “Healthy.”

## Project Goals
Train a Linear Regression model to predict SOH.

Evaluate the model using:
  - R² (coefficient of determination)
  - Mean Squared Error (MSE)
  - Mean Absolute Error (MAE)
    
Classify each battery pack using the 0.6 SOH threshold.

---

## Installation

Clone this repository and install dependencies.  

you can use pip install -r Requirements.txt to do this  

## Usage  
After you clone the repo and download the dependencies you can run the model using  

python pulsebat_linear_regression.py  

This will then show performance metrics of the model such as the  
  - R² (coefficient of determination)
  - Mean Squared Error (MSE)
  - Mean Absolute Error (MAE)
    
And Plots the actual SOH vs the Predicted SOH which will be saved in /plots/ folder
