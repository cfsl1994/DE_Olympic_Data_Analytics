import requests
import boto3
import os

def lambda_handler(event, context):
    # The base URL path for the CSV files
    url_path = os.environ['CSV_URL_PATH']  # Make sure to include trailing slash in the environment variable
    csv_files = ['Athletes.csv', 'Coaches.csv', 'EntriesGender.csv', 'Medals.csv', 'Teams.csv']
    
    # The S3 bucket where the CSV will be uploaded
    s3_bucket = os.environ['S3_BUCKET']
    
    s3 = boto3.client('s3')  # Initialize the S3 client outside of the loop

    for file in csv_files:
        # Construct the full CSV URL
        csv_url = url_path + file
        
        # Use the requests library to download the CSV
        response = requests.get(csv_url)
    
        # Check if the request was successful
        if response.status_code == 200:
            # Get the CSV data
            csv_data = response.content.decode('windows-1252').encode('utf-8')
        
            # Construct the S3 key
            s3_key = f'olympic-data-analytics/{file}'
            
            # Upload the CSV data to S3
            s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=csv_data)
            print(f"File {file} uploaded successfully to {s3_bucket}/{s3_key}")
        else:
            print(f"Failed to download {file}. Status code: {response.status_code}")

    # Return status after processing all files
    return {
        'statusCode': 200,
        'body': 'All files processed'
    }