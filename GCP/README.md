# Olympics_Data_Analytics
## Steps

#### AZURE FACTORY:
###### General configuration
        - Data Factory Name v2 -> data-engineering-data-fact
        - group resources -> data-engineering
        - subscription -> YOUR SUBSCRIPTION
        - Pipelines -> Olympic_Data_Analytics_Factory

###### Copy data Athletes
        - Name -> Athletes
        - Source 
                - Source dataset -> Athletes_Source
                        - Connection:
                        	- Linked service:
                        		- Name -> Athletes_HTTP
                        		- Description -> Athletes_HTTP
                        		- Connect via integration runtime -> AutoResolverIntegrationRuntime
                        		- Base URL -> https://raw.githubusercontent.com/YOUR_GITHUB/main/data/Athletes.csv
                        		- Server certification validation -> Disable
                        		- Authentication type -> Anonymous

                        	- Column type -> Semicolon 
                        	- Row delimiter -> Default (\r\n, or \r\n)
                        	- Encoding -> Default(UTF-8)
                        	- Quote character -> Double quote (")
                        	- Escape character -> Backslash (\)
                        	- First row as header -> Check	
                - Request method -> GET
        - Sink
                - Sink dataset -> Athletes_Destination
                        - Connection:
                                - Linked service:
                                        - Name -> BS_Athletes
                                        - Description -> BS_Athletes
                                        - Connect via integration runtime -> AutoResolverIntegrationRuntime
                                        - Authentication type -> Account key
                                        - Storage account name -> YOUR DATA STAGE BUCKET
                                        - Storage account key -> YOUR DATA STAGE BUCKET KEY
                                        - Endpoint suffix -> core.windows.net
                                        - Test linked service -> check
                                - File path -> YOUR DATA STAGE BUCKET / Directory / Athletes.csv
                                - Column delimiter -> Comma (,)
                                - Row delimiter -> Default (\r\n, or \r\n)
                                - Encoding -> Default(UTF-8)
                        	- Quote character -> Double quote (")
                        	- Escape character -> Backslash (\)
                        	- First row as header -> Check	

###### Copy data Coaches
        - Name -> Coaches
        - Source 
                - Source dataset -> Coaches_Source
                        - Connection:
                        	- Linked service:
                        		- Name -> Coaches_HTTP
                        		- Description -> Coaches_HTTP
                        		- Connect via integration runtime -> AutoResolverIntegrationRuntime
                        		- Base URL -> https://raw.githubusercontent.com/YOUR_GITHUB/main/data/Coaches.csv
                        		- Server certification validation -> Disable
                        		- Authentication type -> Anonymous

                        	- Column type -> Semicolon 
                        	- Row delimiter -> Default (\r\n, or \r\n)
                        	- Encoding -> Default(UTF-8)
                        	- Quote character -> Double quote (")
                        	- Escape character -> Backslash (\)
                        	- First row as header -> Check	
                - Request method -> GET
        - Sink
                - Sink dataset -> Coaches_Destination
                        - Connection:
                                - Linked service:
                                        - Name -> BS_Coaches
                                        - Description -> BS_Coaches
                                        - Connect via integration runtime -> AutoResolverIntegrationRuntime
                                        - Authentication type -> Account key
                                        - Storage account name -> YOUR DATA STAGE BUCKET
                                        - Storage account key -> YOUR DATA STAGE BUCKET KEY
                                        - Endpoint suffix -> core.windows.net
                                        - Test linked service -> check
                                - File path -> YOUR DATA STAGE BUCKET / Directory / Coaches.csv
                                - Column delimiter -> Comma (,)
                                - Row delimiter -> Default (\r\n, or \r\n)
                                - Encoding -> Default(UTF-8)
                        	- Quote character -> Double quote (")
                        	- Escape character -> Backslash (\)
                        	- First row as header -> Check

###### Copy data EntriesGender
        - Name -> EntriesGender
        - Source 
                - Source dataset -> EntriesGender_Source
                        - Connection:
                        	- Linked service:
                        		- Name -> EntriesGender_HTTP
                        		- Description -> EntriesGender_HTTP
                        		- Connect via integration runtime -> AutoResolverIntegrationRuntime
                        		- Base URL -> https://raw.githubusercontent.com/YOUR_GITHUB/main/data/EntriesGender.csv
                        		- Server certification validation -> Disable
                        		- Authentication type -> Anonymous

                        	- Column type -> Semicolon 
                        	- Row delimiter -> Default (\r\n, or \r\n)
                        	- Encoding -> Default(UTF-8)
                        	- Quote character -> Double quote (")
                        	- Escape character -> Backslash (\)
                        	- First row as header -> Check	
                - Request method -> GET
        - Sink
                - Sink dataset -> EntriesGender_Destination
                        - Connection:
                                - Linked service:
                                        - Name -> BS_EntriesGender
                                        - Description -> BS_EntriesGender
                                        - Connect via integration runtime -> AutoResolverIntegrationRuntime
                                        - Authentication type -> Account key
                                        - Storage account name -> YOUR DATA STAGE BUCKET
                                        - Storage account key -> YOUR DATA STAGE BUCKET KEY
                                        - Endpoint suffix -> core.windows.net
                                        - Test linked service -> check
                                - File path -> YOUR DATA STAGE BUCKET / Directory / EntriesGender.csv
                                - Column delimiter -> Comma (,)
                                - Row delimiter -> Default (\r\n, or \r\n)
                                - Encoding -> Default(UTF-8)
                        	- Quote character -> Double quote (")
                        	- Escape character -> Backslash (\)
                        	- First row as header -> Check

###### Copy data Medals
        - Name -> Medals
        - Source 
                - Source dataset -> Medals_Source
                        - Connection:
                        	- Linked service:
                        		- Name -> Medals_HTTP
                        		- Description -> Medals_HTTP
                        		- Connect via integration runtime -> AutoResolverIntegrationRuntime
                        		- Base URL -> https://raw.githubusercontent.com/YOUR_GITHUB/main/data/Medals.csv
                        		- Server certification validation -> Disable
                        		- Authentication type -> Anonymous

                        	- Column type -> Semicolon 
                        	- Row delimiter -> Default (\r\n, or \r\n)
                        	- Encoding -> Default(UTF-8)
                        	- Quote character -> Double quote (")
                        	- Escape character -> Backslash (\)
                        	- First row as header -> Check	
                - Request method -> GET
        - Sink
                - Sink dataset -> Medals_Destination
                        - Connection:
                                - Linked service:
                                        - Name -> BS_Medals
                                        - Description -> BS_Medals
                                        - Connect via integration runtime -> AutoResolverIntegrationRuntime
                                        - Authentication type -> Account key
                                        - Storage account name -> YOUR DATA STAGE BUCKET
                                        - Storage account key -> YOUR DATA STAGE BUCKET KEY
                                        - Endpoint suffix -> core.windows.net
                                        - Test linked service -> check
                                - File path -> YOUR DATA STAGE BUCKET / Directory / Medals.csv
                                - Column delimiter -> Comma (,)
                                - Row delimiter -> Default (\r\n, or \r\n)
                                - Encoding -> Default(UTF-8)
                        	- Quote character -> Double quote (")
                        	- Escape character -> Backslash (\)
                        	- First row as header -> Check

###### Copy data Teams
        - Name -> Teams
        - Source 
                - Source dataset -> Teams_Source
                        - Connection:
                        	- Linked service:
                        		- Name -> Teams_HTTP
                        		- Description -> Teams_HTTP
                        		- Connect via integration runtime -> AutoResolverIntegrationRuntime
                        		- Base URL -> https://raw.githubusercontent.com/YOUR_GITHUB/main/data/Teams.csv
                        		- Server certification validation -> Disable
                        		- Authentication type -> Anonymous

                        	- Column type -> Semicolon 
                        	- Row delimiter -> Default (\r\n, or \r\n)
                        	- Encoding -> Default(UTF-8)
                        	- Quote character -> Double quote (")
                        	- Escape character -> Backslash (\)
                        	- First row as header -> Check	
                - Request method -> GET
        - Sink
                - Sink dataset -> Teams_Destination
                        - Connection:
                                - Linked service:
                                        - Name -> Teams_Medals
                                        - Description -> Teams_Medals
                                        - Connect via integration runtime -> AutoResolverIntegrationRuntime
                                        - Authentication type -> Account key
                                        - Storage account name -> YOUR DATA STAGE BUCKET
                                        - Storage account key -> YOUR DATA STAGE BUCKET KEY
                                        - Endpoint suffix -> core.windows.net
                                        - Test linked service -> check
                                - File path -> YOUR DATA STAGE BUCKET / Directory / Teams.csv
                                - Column delimiter -> Comma (,)
                                - Row delimiter -> Default (\r\n, or \r\n)
                                - Encoding -> Default(UTF-8)
                        	- Quote character -> Double quote (")
                        	- Escape character -> Backslash (\)
                        	- First row as header -> Check

#### AZURE STORAGE:
###### General RAW ZONE STORAGE ACCOUNT
        - storage account -> YOUR RAW ZONE STORAGE ACCOUNT
        - resouce group -> data-engineering
        - subscription -> YOUR SUBSCRIPTION
        - container -> olympic-data-analytics
        - properties -> Data Lake Storage -> Hierarchical namespace

###### General STAGE ZONE STORAGE ACCOUNT
        - storage account -> YOUR STAGE ZONE STORAGE ACCOUNT
        - resouce group -> data-engineering
        - subscription -> YOUR SUBSCRIPTION
        - container -> olympic-data-analytics
        - properties -> Data Lake Storage -> Hierarchical namespace

#### AZURE DATABRICKS:
        - azure databricks service -> data-engineering-databricks
        - resource group -> data-engineering
        - subscription -> YOUR SUBSCRIPTION
###### COMPUTE       
        - name -> olympic-data-analytic's Cluster
        - runtime -> 12.2
        - policy -> Unrestricted
        - access mode -> single user
        - performance -> 12.2 LTS (includes Apache Spark 3.3.2, Scala 2.12) 
        - worker type -> Standar_DS3_V2
        - driver type -> Standar_DS3_V2
        - catalog explorer:
                - storage credentials: 
                        - name -> adls-data-engineering-raw-credential-name-storage:
                                - credential -> managed identity
                                - properties -> YOUR CONNECTOR ID FROM ACCESS CONNECTOR FOR AZURE DATABRICKS - RAW ZONE STORAGE
                        - name -> adls-data-engineering-stage-credential-name-storage:
                                - credential -> managed identity
                                - properties -> YOUR CONNECTOR ID FROM ACCESS CONNECTOR FOR AZURE DATABRICKS - RAW ZONE STORAGE
                - external locations:
                        - name -> adls-data-engineering-raw-external-location:
                                - credential -> adls-data-engineering-raw-credential-name-storage
                                - url -> abfss://olympic-data-analytics@RAW ZONE STORAGE.dfs.core.windows.net/
                        - name -> adls-data-engineering-raw-external-location:
                                - credential -> adls-data-engineering-stage-credential-name-storage
                                - url -> abfss://olympic-data-analytics@STAGE ZONE STORAGE.dfs.core.windows.net/

###### WORKSPACE
        - notebook -> olympic-data-analytics-notebook.ipynb 

###### ACCESS CONNECTOR FOR AZURE DATABRICKS - RAW ZONE STORAGE
        - name -> adls-data-engineering-raw-access-connector
        - resource group -> data-engineering
        - subscription -> YOUR SUBSCRIBER

###### ACCESS CONNECTOR FOR AZURE DATABRICKS - STAGE ZONE STORAGE
        - name -> adls-data-engineering-stage-access-connector
        - resource group -> data-engineering
        - subscription -> YOUR SUBSCRIBER

#### AZURE SYNAPSE ANALYTICS
        - name -> data-engineering-synap
        - type -> synapse workspace
        - resource group -> data-engineering
        - subscription -> YOUR SUBSCRIPTION

###### DATA BASE LAKE
        - name -> olympic_data_analytics_db
        - source -> data external (STAGE ZONE STORAGE)

###### tables athletes
        - general:
                - name -> tbl_athletes
                - link service -> YOUR WORKSPACE SYNAPSE 
                - folder -> olympic-data-analytics/athletes
                - data format -> parquet
                - compression -> none

###### tables coaches
        - general:
                - name -> tbl_coaches
                - link service -> YOUR WORKSPACE SYNAPSE 
                - folder -> olympic-data-analytics/coaches
                - data format -> parquet
                - compression -> none

###### tables entriesgender
        - general:
                - name -> tbl_entriesgender
                - link service -> YOUR WORKSPACE SYNAPSE 
                - folder -> olympic-data-analytics/entriesgender
                - data format -> parquet
                - compression -> none

###### tables medals
        - general:
                - name -> tbl_medals
                - link service -> YOUR WORKSPACE SYNAPSE 
                - folder -> olympic-data-analytics/medals
                - data format -> parquet
                - compression -> none

###### tables teams
        - general:
                - name -> tbl_teams
                - link service -> YOUR WORKSPACE SYNAPSE 
                - folder -> olympic-data-analytics/teams
                - data format -> parquet
                - compression -> none

#### POWER BI
        - At your discretion

## Architecture-Diagram
![Architecture-Diagram](Olympic-Data-Analytics-Azure.jpg)