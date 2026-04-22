import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 10))
    df.plot(x="Year", y="CSIRO Adjusted Sea Level", kind="scatter")


    # Create first line of best fit
    x1 = range(df["Year"].iloc[0], 2051, 1)
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    
    y1 = intercept + slope * pd.Series(x1)
    plt.plot(x1, y1, 'c', label='fitted line 1')
 
    # Create second line of best fit
    recent = df[df["Year"] >= 2000]
    x2 = range(2000, 2051, 1)
    slope2, intercept2, *_ = linregress(recent["Year"], recent["CSIRO Adjusted Sea Level"])
    
    y2 = intercept2 + slope2 * pd.Series(x2)
    plt.plot(x2, y2, 'm', label='fitted line 2')
    

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_predict_plot.png')
    return plt.gca()