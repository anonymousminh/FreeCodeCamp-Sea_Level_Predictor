import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    sea_level_df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(sea_level_df["Year"], sea_level_df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    res = linregress(sea_level_df["Year"], sea_level_df["CSIRO Adjusted Sea Level"])
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = res.slope * x_pred + res.intercept

    plt.plot(x_pred, y_pred, "r")

    # Create second line of best fit
    sea_level_2000_df = sea_level_df[sea_level_df["Year"] >= 2000]

    res_2 = linregress(
        sea_level_2000_df["Year"], sea_level_2000_df["CSIRO Adjusted Sea Level"]
    )
    x_pred2 = pd.Series([i for i in range(2000, 2051)])
    y_pred2 = res_2.slope * x_pred2 + res_2.intercept

    plt.plot(x_pred2, y_pred2, "blue")

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
