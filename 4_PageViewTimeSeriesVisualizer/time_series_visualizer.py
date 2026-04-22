import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', skipinitialspace=True) 

# Clean data
# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
# eliminate the human manlapulation error and Statistical Outlier removal
df = df.loc[(df.value >= df.value.quantile(0.025))
                 & (df.value <= df.value.quantile(0.975)), :]
df.count = lambda numeric_only=True: df.shape[0]

def draw_line_plot():
    # Draw line plot
    df_line = df.reset_index()
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df_line['index'], df_line['value'], color='red')

    # Set the labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = pd.DatetimeIndex(df_bar.date).year
    df_bar['month'] = pd.DatetimeIndex(df_bar.date).month

    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack() 
    
    # Draw bar plot
    # Month names for plotting legend
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ax = df_bar.plot.bar(figsize=(14,7))
    ax.legend(months, title='Months', prop={'size': 8})

    # Set the labels and title
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.tight_layout()




    # Save image and return fig (don't change this part)
    fig = ax.get_figure()
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['date'] = pd.to_datetime(df_box['date'])  # Convert to datetime
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(ncols=2, figsize=(25,8))

    # Year-wise box plot (Trend)
    sns.boxplot(ax=ax[0], x='year', y='value', data=df_box, fliersize= 2, palette='Set2')

    # Set the labels and title
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[0].set_title("Year-wise Box Plot (Trend)")

    # Month-wise box plot (Seasonality)
    sns.boxplot(ax=ax[1], x='month', y='value', data=df_box, order=month_order, fliersize= 2, palette='Set2')


    # Set the labels and title
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    ax[1].set_title("Month-wise Box Plot (Seasonality)")




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
