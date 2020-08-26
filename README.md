# SQL-visualization
Script to visualize SQL queries (default: google bigquery)

This readme is a tutorial of how to use the SQL visualization script to visualize SQL queries. The `qplot` function will help us explore any SQL queries.

```Python
qplot(query, column1, column2=None, w=15, h=5, color='deeppink', data='new_york')
```


> ***PS. The default database in this function is the google bigquery database, if you are using other databases, you will have to modify the database connection lines of code.***

###  Example:
![Example](https://i.ibb.co/2FDBPLG/Screen-Shot-2020-08-26-at-18-19-11.png)

The funcion `qplot` takes 6 parameters:

    1-query: your SQL query
    2-column1: column to plot
    3-column2: 2nd column to plot with respect to column1 (optional)
    4-w= width (default w=15)
    5-h= height (default h=5)
    6-color= color (default color='deeppink')
    7-data = dataset from google cloud BigQuery (if you need to connect to another database, you'll need to modify the connection code)
    

**TUTORIAL:** https://www.kaggle.com/amiiiney/a-ride-through-nyc-sql-queries-visualization
