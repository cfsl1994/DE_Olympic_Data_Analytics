# Olympics_Data_Analytics
## Steps

#### GCP FUNCTION:
###### DETAILS 
        - name -> Olympic_Data_Analytics_Functions
        - memory allocated -> 256 MB
        - CPU -> 167 millis
        - timeout -> 60 seconds

###### SOURCE
        - runtime -> python 3-10
        - entry point -> download_and_upload_to_gcs
        - code -> main.py
        - requirements -> requirements.txt

###### VARIABLES
        - runtime enviroment variables
        - CSV_URL_PATH -> https://raw.githubusercontent.com/YOUR GITHUB/main/data/
        - GCS_BUCKET -> YOUR RAW ZONE GCS

#### GCP STORAGE:
###### RAW ZONE STORAGE
        - GOOGLE STORAGE -> YOUR RAW ZONE STORAGE
        - STORAGE CLASE -> standar
        - OBJECT -> olympic-data-analytics

###### STAGE ZONE STORAGE
        - GOOGLE STORAGE -> YOUR STAGE ZONE STORAGE
        - STORAGE CLASE -> standar
        - OBJECT -> olympic-data-analytics

#### DATAPREP BY TRIFACTA 
        - name -> Olympic_Data_Analytics_DataPrep

###### DATASET ATHLETES
        - Parameters -> gs://YOUR DATA RAW ZONE STORAGE/olympic-data-analytics/Athletes.csv

###### RECIPE ATHLETES
        - Steps -> Convert row 1 to header
                   Rename Name to 'PersonName'
                   Rename NOC to 'Country'

###### OUTPUT ATHLETES
        - Manual Settings:
                - Options:
                        - Enviroment -> Dataflow
                        - Profiling -> yes
                        - Validate schema -> yes
                - Publishing actions
                        - Replace AVRO
                        - Location -> gs://YOUR DATA STAGE ZONE STORAGE/olympic-data-analytics/Athletes.avro 
                        - Settings -> multiples files
                        - Service account -> YOUR SERVICE ACCOUNT

###### DATASET COACHES
        - Parameters -> gs://YOUR DATA RAW ZONE STORAGE/olympic-data-analytics/Coaches.csv

###### RECIPE COACHES
         - Steps -> Convert row 1 to header
                   Rename NOC to 'Country'

###### OUTPUT COACHES
- Manual Settings:
                - Options:
                        - Enviroment -> Dataflow
                        - Profiling -> yes
                        - Validate schema -> yes
                - Publishing actions
                        - Replace AVRO
                        - Location -> gs://YOUR DATA STAGE ZONE STORAGE/olympic-data-analytics/Coaches.avro 
                        - Settings -> multiples files
                        - Service account -> YOUR SERVICE ACCOUNT

###### DATASET MEDALS
        - Parameters -> gs://YOUR DATA RAW ZONE STORAGE/olympic-data-analytics/Medals.csv

###### RECIPE MEDALS
        - Steps -> Rename Team/NOC to 'Team_Country'
                   Rename Rank by Total to 'Rank_by_Total'

###### OUTPUT MEDALS
        - Manual Settings:
                        - Options:
                                - Enviroment -> Dataflow
                                - Profiling -> yes
                                - Validate schema -> yes
                        - Publishing actions
                                - Replace AVRO
                                - Location -> gs://YOUR DATA STAGE ZONE STORAGE/olympic-data-analytics/Medals.avro 
                                - Settings -> multiples files
                                - Service account -> YOUR SERVICE ACCOUNT

###### DATASET TEAMS
        - Parameters -> gs://YOUR DATA RAW ZONE STORAGE/olympic-data-analytics/Teams.csv

###### RECIPE TEAMS
        - Steps -> Convert row 1 to header
                   Rename Name to 'TeamName'
                   Rename NOC to 'Country'

###### OUTPUT TEAMS
        - Manual Settings:
                        - Options:
                                - Enviroment -> Dataflow
                                - Profiling -> yes
                                - Validate schema -> yes
                        - Publishing actions
                                - Replace AVRO
                                - Location -> gs://YOUR DATA STAGE ZONE STORAGE/olympic-data-analytics/Teams.avro 
                                - Settings -> multiples files
                                - Service account -> YOUR SERVICE ACCOUNT

###### DATASET ENTRIESGENDER
        - Parameters -> gs://YOUR DATA RAW ZONE STORAGE/olympic-data-analytics/EntriesGender.csv

###### RECIPE ENTRIESGENDER
        - Steps -> None

###### OUTPUT ENTRIESGENDER
        - Manual Settings:
                        - Options:
                                - Enviroment -> Dataflow
                                - Profiling -> yes
                                - Validate schema -> yes
                        - Publishing actions
                                - Replace AVRO
                                - Location -> gs://YOUR DATA STAGE ZONE STORAGE/olympic-data-analytics/EntriesGender.avro 
                                - Settings -> multiples files
                                - Service account -> YOUR SERVICE ACCOUNT

#### GCP LOOKER
        - At your discretion

## Architecture-Diagram
![Architecture-Diagram](Olympic-Data-Analytics-Gcp.jpg)