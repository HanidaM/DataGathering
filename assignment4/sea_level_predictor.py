import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")
    
    df["CSIRO Adjusted Sea Level"] *= 0.0254
    df["Lower Error Bound"] *= 0.0254
    df["Upper Error Bound"] *= 0.0254

    fig, ax = plt.subplots(figsize=(10, 10))
    df.plot(x="Year", y="CSIRO Adjusted Sea Level", kind="scatter", ax=ax, label="Data")

    x1 = range(df["Year"].iloc[0], 2050, 1)
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    ax.plot(x1, intercept + slope * pd.Series(x1), 'r', label='Fitted Line 1880-2050')

    recent_data = df[df["Year"] >= 2000]
    x2 = range(2000, 2050, 1)
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
        recent_data["Year"], recent_data["CSIRO Adjusted Sea Level"])
    ax.plot(x2, intercept_recent + slope_recent * pd.Series(x2), 'g', label='Fitted Line 2000-2050')

    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (meters)")
    ax.legend()

    plt.savefig('sea_level_plot.png')
    return ax
