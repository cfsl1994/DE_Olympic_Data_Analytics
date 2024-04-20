import requests
from google.cloud import storage
import os

def download_and_upload_to_gcs(request):
    # The base URL path for the CSV files
    url_path = os.environ.get('CSV_URL_PATH')  # Ensure there is a trailing slash
    csv_files = ['Athletes.csv', 'Coaches.csv', 'EntriesGender.csv', 'Medals.csv', 'Teams.csv']
    
    # The GCS bucket where the CSV will be uploaded
    gcs_bucket = os.environ.get('GCS_BUCKET')
    
    # Initialize the GCS client
    storage_client = storage.Client()
    bucket = storage_client.bucket(gcs_bucket)

    for file in csv_files:
        # Construct the full CSV URL
        csv_url = url_path + file
        
        # Use the requests library to download the CSV
        response = requests.get(csv_url)
    
        # Check if the request was successful
        if response.status_code == 200:
            # Get the CSV data
            csv_data = response.content.decode('windows-1252').encode('utf-8')
        
            # Construct the GCS blob name
            blob_name = f'olympic-data-analytics/{file}'
            blob = bucket.blob(blob_name)
            
            # Upload the CSV data to GCS
            blob.upload_from_string(csv_data, content_type='text/csv')
            print(f"File {file} uploaded successfully to gs://{gcs_bucket}/{blob_name}")
        else:
            print(f"Failed to download {file}. Status code: {response.status_code}")

    # Return status after processing all files
    return 'All files processed', 200