#===============================================================================
# Create 5-year ACS Tables for IntearctVTrans
#===============================================================================
# This script pulls statistics from calendar import LocaleTextCalendar
# from the 5-Year American Community Survey that are 
# most relevant to determining the VTrans Mid-Term Needs for display on 
# InteractVTrans.
#
# Before running, it's important to ensure that the data in StatsDict.py is
# accurate, as the tables are built using that file as a reference.
#
# It will create a CSV file for each of the items in the ACS_Tables list located
# in StatsDict.py.
#===============================================================================
# Written for ArcGIS Pro Python Environment
# By Dan Fourquet
# September 2022
#===============================================================================

import pandas as pd
# import arcpy
import os
# import pandas as pd
import requests

from StatsDict import ACS_Tables

# Output directory for CSV files
output_dir = r"C:\Users\daniel.fourquet\Documents\Tasks\ACS-Tables\Output"

if not os.path.exists(output_dir):
    raise Exception("Output directory does not exist.")


URL_base = "https://api.census.gov/data/2020/acs/acs5?"
URL_for = "&for=block%20group:*&in=state:51%20county:*"
print("\n==========\n")

for table in ACS_Tables:
    print(f"Downloading {table['name']}")

    name = table['name']
    alias = table['alias']
    data = table['data']
    geography = table['geography']

    
    # Create URL
    if geography == "block group":
        URL_for = "&for=block%20group:*&in=state:51%20county:*"
    
    if geography == "county":
        URL_for = "&for=county:*&in=state:*"

    if table['fullTable']:
        # Download entire table
        URL_get = "get="
        URL_get += f"group({table['fullTable']}),"
    else:
        URL_get = "get=NAME,GEO_ID,"
        # Download individual statistics
        for stat in data.keys():
            URL_get += f"{stat},"

    URL = f"{URL_base}{URL_get[:-1]}{URL_for}"
    print(f"    URL:\n        {URL}")


    # Get data from URL
    try:
        response = requests.get(URL)
        data = list(response.json())
    except Exception as e:
        print("Error creating URL\n--")
        print(e)
        print("\n==========\n")
        continue


    # Create DataFrame
    try:
        columns = data[0]
        data = data[1:]
        df = pd.DataFrame(data,columns=columns)
        df = df.apply(pd.to_numeric, errors='ignore', downcast='integer')

        # Apply functions
        if table['functions']:
            for f in table['functions']:
                funcName = f['name']
                funcAlias = f['alias']
                funcOperation = f['operation']
                funcStatistics = f['statistics']

                print(f"    Calculating {funcName}")
                if funcOperation == "sum":
                    df[funcName] = df[funcStatistics].sum(axis=1)
    except Exception as e:
        print("Error creating DataFrame\n--")
        print(e)
        print("\n==========\n")
        continue


    # Save CSV
    try:
        df.to_csv(f"{output_dir}\\{name}.csv",index=False)

    except Exception as e:
        print("Error creating CSV\n--")
        print(e)
        print("\n==========\n")
        continue

    
    
    print("\n==========\n")
    

