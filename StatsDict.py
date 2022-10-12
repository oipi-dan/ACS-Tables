"""
{
        "name": Name of the table in the output csv and gdb,
        "alias": Alias of table in gdb,
        "geography": Geography level of the dataset (eg county, block group)
        "fullTable": If downloading a full table, the name of the table goes here
                     Note that the API allows a maximum of 50 stats, so if we need
                     more than that, we need to download the whole table
        "data": {
            Statistic Name: Statistic alias,
            Statistic Name: Statistic alias,
            Statistic Name: Statistic alias,
            Statistic Name: Statistic alias
        },
        "functions" [ # Additional columns added by performing functions on other columns
            {
                "name": column name,
                "alias": column alias
                "operation": sum or percent
                "statistics": [for sum: list of statistics to apply operation to] or [for percent: part, whole],
            }
        ]
    }
"""


ACS_Tables = [
    {
        "name": "Population_Age_Sex",
        "alias": "Population by Age and Sex",
        "geography": "block group",
        "fullTable": None,
        "data": {
            # Sex by Age
            "B01001_002E": "Total Male",
            "B01001_003E": "Males Under 5 years",
            "B01001_004E": "Males 5 to 9 years",
            "B01001_005E": "Males 10 to 14 years",
            "B01001_006E": "Males 15 to 17 years",
            "B01001_007E": "Males 18 and 19 years",
            "B01001_008E": "Males 20 years",
            "B01001_009E": "Males 21 years",
            "B01001_010E": "Males 22 to 24 years",
            "B01001_011E": "Males 25 to 29 years",
            "B01001_012E": "Males 30 to 34 years",
            "B01001_013E": "Males 35 to 39 years",
            "B01001_014E": "Males 40 to 44 years",
            "B01001_015E": "Males 45 to 49 years",
            "B01001_016E": "Males 50 to 54 years",
            "B01001_017E": "Males 55 to 59 years",
            "B01001_018E": "Males 60 and 61 years",
            "B01001_019E": "Males 62 to 64 years",
            "B01001_020E": "Males 65 and 66 years",
            "B01001_021E": "Males 67 to 69 years",
            "B01001_022E": "Males 70 to 74 years",
            "B01001_023E": "Males 75 to 79 years",
            "B01001_024E": "Males 80 to 84 years",
            "B01001_025E": "Males 85 years and over",
            "B01001_026E": "Total Female",
            "B01001_027E": "Females Under 5 years",
            "B01001_028E": "Females 5 to 9 years",
            "B01001_029E": "Females 10 to 14 years",
            "B01001_030E": "Females 15 to 17 years",
            "B01001_031E": "Females 18 and 19 years",
            "B01001_032E": "Females 20 years",
            "B01001_033E": "Females 21 years",
            "B01001_034E": "Females 22 to 24 years",
            "B01001_035E": "Females 25 to 29 years",
            "B01001_036E": "Females 30 to 34 years",
            "B01001_037E": "Females 35 to 39 years",
            "B01001_038E": "Females 40 to 44 years",
            "B01001_039E": "Females 45 to 49 years",
            "B01001_040E": "Females 50 to 54 years",
            "B01001_041E": "Females 55 to 59 years",
            "B01001_042E": "Females 60 and 61 years",
            "B01001_043E": "Females 62 to 64 years",
            "B01001_044E": "Females 65 and 66 years",
            "B01001_045E": "Females 67 to 69 years",
            "B01001_046E": "Females 70 to 74 years",
            "B01001_047E": "Females 75 to 79 years",
            "B01001_048E": "Females 80 to 84 years",
            "B01001_049E": "Females 85 years and over",
        },
        "functions": [

            {
                "name": "Pop_Total",
                "alias": "Total Population",
                "operation": "sum",
                "statistics": ["B01001_002E","B01001_026E"],
            },
            {
                "name": "Pop_18_64",
                "alias": "Population 18-64",
                "operation": "sum",
                "statistics": ["B01001_007E","B01001_008E","B01001_009E","B01001_010E","B01001_011E","B01001_012E","B01001_013E","B01001_014E","B01001_015E","B01001_016E","B01001_017E","B01001_018E","B01001_019E","B01001_031E","B01001_032E","B01001_033E","B01001_034E","B01001_035E","B01001_036E","B01001_037E","B01001_038E","B01001_039E","B01001_040E","B01001_041E","B01001_042E","B01001_043E"],
            },
            {
                "name": "Pop_65_Plus",
                "alias": "Population 65+",
                "operation": "sum",
                "statistics": ["B01001_044E","B01001_045E","B01001_046E","B01001_047E","B01001_048E","B01001_049E","B01001_020E","B01001_021E","B01001_022E","B01001_023E","B01001_024E","B01001_025E"],
            },
            {
                "name": "Pop_75_Plus",
                "alias": "Population 75+",
                "operation": "sum",
                "statistics": ["B01001_047E","B01001_048E","B01001_049E","B01001_023E","B01001_024E","B01001_025E"],
            }
        ]
    },
    {
        "name": "No_Vehicles_Available",
        "alias": "Households with No Vehicle Available",
        "geography": "tract",
        "fullTable": None,
        "data": {
            "B08201_001E": "Total Households",
            "B08201_002E": "Households with no vehicle available"
        },
        "functions": [
            {
                "name": "Pct_No_Vehicle",
                "alias": "Percent of households with no vehicle available",
                "operation": "percent",
                "statistics": ["B08201_002E","B08201_001E"],
            },
        ]
    }
]