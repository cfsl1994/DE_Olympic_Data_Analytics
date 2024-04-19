# Olympics_Data_Analytics
## Steps


##### AWS LAMBDA:
###### General configuration
        - Timeout -> 5 min 0 sec
        - Memory -> 128 MB
        - SnapStart -> None
        - Ephemeral storage -> 512 MB

###### Enviroment variables
        - key -> CSV_URL_PATH 
        - value -> https://raw.githubusercontent.com/YOUR_GITHUB/main/data/
        - key -> S3_BUCKET
        - value -> YOUR BUCKET

## Architecture-Diagram
![Architecture-Diagram](Olympic-Data-Analytics-Aws.jpg)