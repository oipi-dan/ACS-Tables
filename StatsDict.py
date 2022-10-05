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
                "operation": [sum], Only sum available right now
                "statistics": [list of statistics to apply operation to],
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
        "name": "Hispanic_Latino_Origin",
        "alias": "Hispanic or Latino Origin",
        "geography": "block group",
        "fullTable": None,
        "data": {
            "B03002_012E": "Total Hispanic or Latino",
            "B03002_013E": "Hispanic or Latino - White alone",
            "B03002_014E": "Hispanic or Latino - Black or African American alone",
            "B03002_015E": "Hispanic or Latino - American Indian and Alaska Native alone",
            "B03002_016E": "Hispanic or Latino - Asian alone",
            "B03002_017E": "Hispanic or Latino - Native Hawaiian and Other Pacific Islander alone",
            "B03002_018E": "Hispanic or Latino - Some other race alone",
            "B03002_019E": "Hispanic or Latino - Two or more races",
            "B03002_020E": "Hispanic or Latino - Two races including Some other race",
            "B03002_021E": "Hispanic or Latino - Two races excluding Some other race, and three or more races"
        },
        "functions": None
    },
    {
        "name": "Ratio_Income_Poverty_Level",
        "alias": "Ratio of Income to Poverty Level",
        "geography": "block group",
        "fullTable": None,
        "data": {
            "C17002_002E": "Under .50",
            "C17002_003E": ".50 to .99",
            "C17002_004E": "1.00 to 1.24",
            "C17002_005E": "1.25 to 1.49",
            "C17002_006E": "1.50 to 1.84",
            "C17002_007E": "1.85 to 1.99",
            "C17002_008E": "2.00 and over"
        },
        "functions": None
    },
    {
        "name": "Transportation_To_Work",
        "alias": "Means of Transportation to Work by Travel Time to Work",
        "geography": "county",
        "fullTable": "B08534",
        "data": {
            "B08534_001E": "Total Commuters",
            "B08534_002E": "Commuters (< 10 mins)",
            "B08534_003E": "Commuters (10 to 14 mins)",
            "B08534_004E": "Commuters (15 to 19 mins)",
            "B08534_005E": "Commuters (20 to 24 mins)",
            "B08534_006E": "Commuters (25 to 29 mins)",
            "B08534_007E": "Commuters (30 to 34 mins)",
            "B08534_008E": "Commuters (35 to 44 mins)",
            "B08534_009E": "Commuters (45 to 59 mins)",
            "B08534_010E": "Commuters (> 60 mins)",
            "B08534_021E": "Total Drove alone",
            "B08534_022E": "Drove alone (< 10 mins)",
            "B08534_023E": "Drove alone (10 to 14 mins)",
            "B08534_024E": "Drove alone (15 to 19 mins)",
            "B08534_025E": "Drove alone (20 to 24 mins)",
            "B08534_026E": "Drove alone (25 to 29 mins)",
            "B08534_027E": "Drove alone (30 to 34 mins)",
            "B08534_028E": "Drove alone (35 to 44 mins)",
            "B08534_029E": "Drove alone (45 to 59 mins)",
            "B08534_030E": "Drove alone (> 60 minutes)",
            "B08534_031E": "Carpooled",
            "B08534_032E": "Carpooled (< 10 mins)",
            "B08534_033E": "Carpooled (10 to 14 mins)",
            "B08534_034E": "Carpooled (15 to 19 mins)",
            "B08534_035E": "Carpooled (20 to 24 mins)",
            "B08534_036E": "Carpooled (25 to 29 mins)",
            "B08534_037E": "Carpooled (30 to 34 mins)",
            "B08534_038E": "Carpooled (35 to 44 mins)",
            "B08534_039E": "Carpooled (45 to 59 mins)",
            "B08534_040E": "Carpooled (> 60  mins)",
            "B08534_061E": "Total Public transportation (excluding taxicab)",
            "B08534_062E": "Public transportation (< 10 mins)",
            "B08534_063E": "Public transportation (10 to 14 mins)",
            "B08534_064E": "Public transportation (15 to 19 mins)",
            "B08534_065E": "Public transportation (20 to 24 mins)",
            "B08534_066E": "Public transportation (25 to 29 mins)",
            "B08534_067E": "Public transportation (30 to 34 mins)",
            "B08534_068E": "Public transportation (35 to 44 mins)",
            "B08534_069E": "Public transportation (45 to 59 mins)",
            "B08534_070E": "Public transportation (> 60 mins)",
            "B08534_101E": "Total Walked",
            "B08534_102E": "Walked (< 10 mins)",
            "B08534_103E": "Walked (10 to 14 mins)",
            "B08534_104E": "Walked (15 to 19 mins)",
            "B08534_105E": "Walked (20 to 24 mins)",
            "B08534_106E": "Walked (25 to 29 mins)",
            "B08534_107E": "Walked (30 to 34 mins)",
            "B08534_108E": "Walked (35 to 44 mins)",
            "B08534_109E": "Walked (45 to 59 mins)",
            "B08534_110E": "Walked (> 60 mins)",
            "B08534_111E": "Total Taxicab, motorcycle, bicycle, or other means",
            "B08534_112E": "Taxicab, motorcycle, bicycle, or other (< 10 mins)",
            "B08534_113E": "Taxicab, motorcycle, bicycle, or other (10 to 14 mins)",
            "B08534_114E": "Taxicab, motorcycle, bicycle, or other (15 to 19 mins)",
            "B08534_115E": "Taxicab, motorcycle, bicycle, or other (20 to 24 mins)",
            "B08534_116E": "Taxicab, motorcycle, bicycle, or other (25 to 29 mins)",
            "B08534_117E": "Taxicab, motorcycle, bicycle, or other (30 to 34 mins)",
            "B08534_118E": "Taxicab, motorcycle, bicycle, or other (35 to 44 mins)",
            "B08534_119E": "Taxicab, motorcycle, bicycle, or other (45 to 59 mins)",
            "B08534_120E": "Taxicab, motorcycle, bicycle, or other (> 60 mins)"
        },
        "functions": None
    },
    {
        "name": "Employment_Status",
        "alias": "Employment Status for the Population 16 Years and Over",
        "geography": "block group",
        "fullTable": None,
        "data": {
            # Employment Status for the Population 16 Years and Over
            "B23025_001E": "Total",
            "B23025_002E": "In labor force:",
            "B23025_003E": "Civilian labor force:",
            "B23025_004E": "Employed",
            "B23025_005E": "Unemployed",
            "B23025_006E": "Armed Forces",
            "B23025_007E": "Not in labor force"
        },
        "functions": None
    },
    {
        "name": "Number_Of_Vehicles",
        "alias": "Aggregate Number of Vehicles Used in Commuting",
        "geography": "block group",
        "fullTable": None,
        "data": {
            "B08015_001E": "Aggregate number of vehicles (Car, Truck, or Van) Used in Commuting"
        },
        "functions": None
    }
]