import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv", skipinitialspace=True) 

# 2
# Add 'overweight' column
# value 0 if NOT overweight and the value 1 if overweight
BMI = df['weight']/((df['height']/100)**2) 
BMI_over_25 = BMI > 25
df['overweight'] = BMI_over_25.astype(int)

# 3
# Normalize data by making 0 always good and 1 always bad. 
# If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1

df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['gluc'] == 1, 'gluc'] = 0

df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] > 1, 'gluc'] = 1

# 4
def draw_cat_plot():
    # 5
    xaxis =['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=xaxis)


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7
    chart = sns.catplot(data=df_cat, kind="bar", x="variable", y="total", hue="value", col="cardio")


    # 8
    fig = chart.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    # Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data
    # eliminate the human manlapulation error and Statistical Outlier removal in weight and height
    df_heat = df.loc[(df.ap_lo <= df.ap_hi)
                 & (df.height >= df.height.quantile(0.025))
                 & (df.height <= df.height.quantile(0.975))
                 & (df.weight >= df.weight.quantile(0.025))
                 & (df.weight <= df.weight.quantile(0.975)), :]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)



    # 14
    fig, ax = plt.subplots(figsize=(15, 10))

    # 15
    ax = sns.heatmap(corr, mask=mask, annot=True, cmap='mako', fmt=".1f")



    # 16
    fig.savefig('heatmap.png')
    return fig
