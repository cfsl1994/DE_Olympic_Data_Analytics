# Olympics_Data_Analytics
## Steps

#### AWS LAMBDA:
###### General configuration
        - Timeout -> 5 min 0 sec
        - Memory -> 128 MB
        - SnapStart -> None
        - Ephemeral storage -> 512 MB

###### Runtime settings  
        - Runtime -> Python 3.10
        - Handler -> lambda_function.lambda_handler
        - Architecture -> x86_64

###### Enviroment variables
        - key -> CSV_URL_PATH 
        - value -> https://raw.githubusercontent.com/YOUR_GITHUB/main/data/
        - key -> S3_BUCKET
        - value -> YOUR BUCKET

###### Code
        - code -> lambda_function.py

###### Layers
        - name -> Olympic_Data_Analytics_Layer
        - layer -> requests-lib.zip
        - Layer version -> 2
        - Compatible runtimes -> python3.10
        - Compatible architectures -> x86_64

## Architecture-Diagram
![Architecture-Diagram](Olympic-Data-Analytics-Aws.jpg)