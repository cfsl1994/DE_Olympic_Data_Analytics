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

#### AWS S3:
###### General S3 Raw Data
        - bucket -> YOUR BUCKET RAW DATA
        - objetct -> olympic-data-analytics/

###### General S3 Raw Data
        - bucket -> YOUR BUCKET STAGE DATA
        - objetct -> olympic-data-analytics/

#### AWS GLUE:
###### Basic properties
        - Etl job name -> Olympic_Data_Analytics_Glue_Job
        - IAM Role -> YOUR IAM ROLE
        - Type -> Spark
        - Glue version -> Glue 4.0 - Supports spark 3.3, Scala 2, Python 3
        - Language -> Python 3
        - Worker type -> G 1X
        
###### Advanced properties
        - Script path -> YOUR SCRIPT PATH BUCKET
        - Spark UI logs path -> YOUR LOG PATH BUCKET

## Architecture-Diagram
![Architecture-Diagram](Olympic-Data-Analytics-Aws.jpg)