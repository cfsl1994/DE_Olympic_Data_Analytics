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

## Architecture-Diagram
![Architecture-Diagram](Olympic-Data-Analytics-Azure.jpg)