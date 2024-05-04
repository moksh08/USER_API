# data_analysis_app/views.py
from django.shortcuts import render, HttpResponse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from io import StringIO

def data_tab(request):
    # Read Titanic dataset from CSV
    df = pd.read_csv("C:\\Users\\moksh\\Downloads\\cleaned_flight_data (1).csv")
 # Get the first ten rows of the dataset
    df_first_ten = df.head(10)

    # Get information about the columns (data types, non-null counts, null counts)
    columns_info = pd.DataFrame({
        'Column Name': df.columns,
        'Data Type': df.dtypes,
        'Non-Null Count': df.notnull().sum(),
        'Null Count': df.isnull().sum()
    })

    # Convert DataFrame to HTML for rendering in template
    table_html = df_first_ten.to_html(classes='table table-striped-columns table-secondary')

    # Include the columns information in the HTML template
    columns_info_html = f"{columns_info.to_html(classes='table table-striped-columns table-info', index=False)}"

    return render(request, 'data_tab.html', {'table_html': table_html, 'columns_info_html': columns_info_html})
  
  
def descriptive_statistics_tab(request):
    # Read Titanic dataset from CSV
    df = pd.read_csv("C:\\Users\\moksh\\Downloads\\cleaned_flight_data (1).csv")
    
    # Perform descriptive statistics using pandas
    descriptive_stats = df.describe().to_html(classes='table table-striped-columns table-info')

    return render(request, 'descriptive_statistics_tab.html', {'descriptive_stats': descriptive_stats})

def exploratory_data_analysis_tab(request):
    # Set a non-interactive backend for matplotlib
    plt.switch_backend('agg')

    # Read Titanic dataset from CSV
    df = pd.read_csv("C:\\Users\\moksh\\Downloads\\cleaned_flight_data (1).csv")
    

    # Example: Countplot of 'Sex'
    plot1 = sns.countplot(x='airline', data=df)
    plt.title('Count of Flights by Airline')
    plt.xlabel('Airline')
    plt.ylabel('Count')
    
    # Save plot to BytesIO
    plot1_image = BytesIO()
    plot1.figure.savefig(plot1_image, format='png')
    plot1_base64 = base64.b64encode(plot1_image.getvalue()).decode('utf-8')

    # Example: Age distribution
    plot2 = sns.histplot(x='price', data=df, bins=20, kde=True)
    plt.title('Price Distribution of Flights')
    plt.xlabel('Price')
    plt.ylabel('Count')
    
    # Save plot to BytesIO
    plot2_image = BytesIO()
    plot2.figure.savefig(plot2_image, format='png')
    plot2_base64 = base64.b64encode(plot2_image.getvalue()).decode('utf-8')



    return render(request, 'exploratory_data_analysis_tab.html', {'plot1': plot1_base64, 'plot2': plot2_base64})



def export_to_csv(request):
    # Read Titanic dataset from CSV
    df = pd.read_csv("C:\\Users\\DELL\\Downloads\\titanic.csv")

    # Generate CSV file
    csv_file = df.to_csv(index=False)

    # Create HTTP response with CSV file
    response = HttpResponse(csv_file, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="titanic_data.csv"'
    
    return response