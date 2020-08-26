import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from google.cloud import bigquery

def qplot(query, column1, column2=None, w=15, h=5, color='deeppink', data='new_york'):
    """
    qplot is a function to plot SQL queries (Google cloud BigQuery).
    
     Parameters:
    1-query: your SQL query
    2-column1: column to plot
    3-column2: 2nd column to plot with respect to column1 (optional)
    4-w= width (default w=15)
    5-h= height (default h=5)
    6-color= color (default color='deeppink')
    7-data = dataset from google cloud BigQuery (if you need to connect to another database, you'll need to modify the connection code)
    
    SOURCE: https://www.kaggle.com/amiiiney/sql-visualization-script/
    CONTACT: amineyamlahi@gmail.com
    """
    
    def plotc(data, column, width=10, height=6, color=('silver', 'gold','lightgreen','skyblue','lightpink'), edgecolor='black'):
    
        fig, ax = plt.subplots(figsize=(width,height))
        title_cnt=data[column].value_counts().sort_values(ascending=False).reset_index()
        mn= ax.barh(title_cnt.iloc[:,0], title_cnt.iloc[:,1], color=sns.color_palette('Greens',len(title_cnt)))

        tightout= 0.008*max(title_cnt[column])
        ax.set_title(f'Count of {column}', fontsize=15, weight='bold' )
        ax.set_ylabel(f"{column}", weight='bold', fontsize=12)
        ax.set_xlabel('Count', weight='bold')
        if len(data[column].unique()) < 17:
            plt.xticks(rotation=65)
        else:
            plt.xticks(rotation=90)
        for i in ax.patches:
            ax.text(i.get_width()+ tightout, i.get_y()+0.1, str(round((i.get_width()), 2)),
             fontsize=10, fontweight='bold', color='grey')
        return

    plt.style.use('ggplot')
    #Connect to the google cloud database
    client = bigquery.Client()
    dataset_ref = client.dataset(data, project="bigquery-public-data")
    df = client.query(query).result().to_dataframe()
    #df=pd.read_sql(s, pconn) This code is for ibm database
    if column2 == None:
            if df[column1].dtype != object:
                plt.figure(figsize=(w,h))
                plt.hist(df[column1],color=color, edgecolor='black')
                plt.xlabel(f"{column1}", weight='bold', fontsize=12)
                plt.ylabel("Count", weight='bold', fontsize=12)
                plt.title(f"Histogram of {column1}",weight='bold', fontsize=14)
                plt.xticks(weight='bold')
                plt.yticks(weight='bold')
            
                if len(df[column1].unique()) < 17 and df[column1].dtype== object:
                    plt.xticks(rotation=65)
                else:
                    if df[column1].dtype== object:
                        plt.xticks(rotation=90)
                    elif df[column1].dtype!= object:
                        plt.xticks(rotation=0)
            else:
                plotc(df,column1, height=7, width=10)
    
    else:
            
        if df[column1].dtype == object and df[column2].dtype == object:
                plt.figure(figsize=(w,h))
                plt.scatter(df[column1], df[column2], color=color)
                plt.xlabel(f"{column1}", weight='bold', fontsize=12)
                plt.ylabel(f"{column2}", weight='bold', fontsize=12)
            
                if df[column1].dtype==object and df[column2].dtype != object:
                    plt.title(f'Count of {column1} with respect to {column2}', fontsize=15, weight='bold' )
                else:
                    plt.title(f'Count of {column2} with respect to {column1}', fontsize=15, weight='bold' )
                    if len(df[column1].unique()) < 17 and df[column1].dtype== object:
                        plt.xticks(rotation=65)
                        
                    else:
                        plt.xticks(rotation=90)
                        
        
        else:
            plt.figure(figsize=(w,h))
            plt.scatter(x=df[column1], y=df[column2], color=color, alpha=0.5)
            plt.xlabel(f"{column1}", weight='bold', fontsize=12)
            plt.ylabel(f"{column2}", weight='bold', fontsize=12)
            plt.title(f'Scatter plot of {column1} and {column2}', fontsize=15, weight='bold' )
            if len(df[column1].unique()) < 17 and df[column1].dtype== object:
                plt.xticks(rotation=65)
            else:
                if df[column1].dtype== object:
                    plt.xticks(rotation=90)
    
        
    return plt.show()