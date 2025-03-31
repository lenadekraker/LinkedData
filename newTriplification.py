from rdflib import Graph, URIRef, Literal, Namespace, RDF, XSD
import pandas as pd

# Loading in Turtle file, from Protégé
g = Graph()
g.parse("Final.ttl", format = "turtle")

# Loading in the data in different csv's
agri = pd.read_csv("agricultureSector.csv", delimiter=",", skiprows=4)
gdp = pd.read_csv("GDP.csv", delimiter=",")
gdp = gdp.drop_duplicates(subset="country", keep="last") # Keep only the last occurrence of each country
globalEdu = pd.read_csv("Global_Education.csv", delimiter=",", encoding="ISO-8859-1")
indu = pd.read_csv("industrySector.csv", delimiter=",", skiprows = 4)
lifeExp = pd.read_csv("life expectancy.csv", delimiter=",")
lifeExp = lifeExp.drop_duplicates(subset = "Country Name", keep = "last")
serv = pd.read_csv("serviceSector.csv", delimiter=",", skiprows = 4)
popu = pd.read_csv("Population.csv", delimiter = "," )
popu = popu.iloc[:-6]  # Remove the last 6 rows


# Get namespaces from the ontology 
EX = Namespace("http://example.org/educationOntology#")
DP = Namespace("http://dbpedia.org/")
GN = Namespace("http://www.geonames.org/ontology#")
ISO3 = Namespace("http://ontology.eil.utoronto.ca/ISO37120.owl#")
DPV = Namespace("http://www.w3.org/ns/dpv#")
SCHEMA = Namespace("http://schema.org/")

# Bind namespaces to the graph
g.bind("ex", EX)
g.bind("dp", DP)
g.bind("gn", GN)
g.bind("iso3", ISO3)
g.bind("dpv", DPV)
g.bind("schema", SCHEMA)

# For names, that can be written different ways
country_name_corrections = {
    "The Gambia": "Gambia",  
    "USA": "United States",
    "UK": "United Kingdom",
}

def normalize_country_name(name):
    name = name.strip()  # Remove extra spaces
    return country_name_corrections.get(name, name).replace(",", "")

globalEdu["Countries and areas"] = globalEdu["Countries and areas"].apply(normalize_country_name)
valid_countries = set(globalEdu["Countries and areas"])  # Only allow these countries

# Add all classes
# Define classes explicitly
g.add((SCHEMA.Country, RDF.type, SCHEMA.Class))
g.add((EX.Population, RDF.type, SCHEMA.Class))
g.add((EX.Education, RDF.type, SCHEMA.Class))
g.add((EX.Health, RDF.type, SCHEMA.Class))
g.add((EX.Economy, RDF.type, SCHEMA.Class))
g.add((EX.Sector, RDF.type, SCHEMA.Class))
g.add((EX.CompletionRate, RDF.type, SCHEMA.Class))


# Loop through CSV Global Education and add triples
globalEdu["Countries and areas"] = globalEdu["Countries and areas"].apply(normalize_country_name)
for _, row in globalEdu.iterrows():
    country_name = row["Countries and areas"].replace(" ", "_").replace(",", "") 
    country_uri = URIRef(EX + country_name)

    g.add((country_uri, RDF.type, SCHEMA.Country))

    # Adding country, longitude and latitude
    g.add((country_uri, GN.name, Literal(row["Countries and areas"], datatype = XSD.string)))
    g.add((country_uri, GN.lat, Literal(row["Latitude "], datatype = XSD.double)))
    g.add((country_uri, GN.long, Literal(row["Longitude"], datatype = XSD.double)))

    economy_uri = URIRef(EX + country_name + "_Economy")
    g.add((economy_uri, RDF.type, EX.Economy))
    g.add((economy_uri, EX.hasEconomy, economy_uri))
    g.add((economy_uri, ISO3["5.1"], Literal(row["Unemployment_Rate"], datatype=XSD.double)))
    
    completion_uri = URIRef(EX + country_name + "_CompletionRate")
    g.add((completion_uri, RDF.type, EX.CompletionRate))
    g.add((country_uri, EX.hasCompletionRate, completion_uri))  # Link to country   
    g.add((completion_uri, EX.completionRatePrimaryFemale, Literal(row["Completion_Rate_Primary_Female"], datatype=XSD.double)))
    g.add((completion_uri, EX.completionRatePrimaryMale, Literal(row["Completion_Rate_Primary_Male"], datatype=XSD.double)))
    g.add((completion_uri, EX.completionRateLowerSecondaryFemale, Literal(row["Completion_Rate_Lower_Secondary_Female"], datatype =XSD.double)))
    g.add((completion_uri, EX.completionRateLowerSecondaryMale, Literal(row["Completion_Rate_Lower_Secondary_Male"], datatype =XSD.double)))
    g.add((completion_uri, EX.completionRateUpperSecondaryFemale, Literal(row["Completion_Rate_Upper_Secondary_Female"], datatype =XSD.double)))
    g.add((completion_uri, EX.completionRateUpperSecondaryMale, Literal(row["Completion_Rate_Upper_Secondary_Male"], datatype =XSD.double)))
    
    out_of_school_uri = URIRef(EX + country_name + "_OutOfSchoolRate")
    g.add((out_of_school_uri, RDF.type, EX.OutOfSchoolRate))
    g.add((country_uri, EX.hasOutOfSchoolRate, out_of_school_uri))  # Link to country
    g.add((out_of_school_uri, EX.outOfSchoolRatePrePrimaryFemale, Literal(row["OOSR_Pre0Primary_Age_Female"], datatype =XSD.double)))
    g.add((out_of_school_uri, EX.outOfSchoolRatePrePrimaryMale, Literal(row["OOSR_Pre0Primary_Age_Male"], datatype =XSD.double)))
    g.add((out_of_school_uri, EX.outOfSchoolRatePrimaryFemale, Literal(row["OOSR_Primary_Age_Female"], datatype =XSD.double)))
    g.add((out_of_school_uri, EX.outOfSchoolRatePrimaryMale, Literal(row["OOSR_Primary_Age_Male"], datatype =XSD.double)))
    g.add((out_of_school_uri, EX.outOfSchoolRateLowerSecondaryFemale, Literal(row["OOSR_Lower_Secondary_Age_Female"], datatype =XSD.double)))
    g.add((out_of_school_uri, EX.outOfSchoolRateLowerSecondaryMale, Literal(row["OOSR_Lower_Secondary_Age_Male"], datatype =XSD.double)))
    g.add((out_of_school_uri, EX.outOfSchoolRateUpperSecondaryFemale, Literal(row["OOSR_Upper_Secondary_Age_Female"], datatype =XSD.double)))
    g.add((out_of_school_uri, EX.outOfSchoolRateUpperSecondaryMale, Literal(row["OOSR_Upper_Secondary_Age_Male"], datatype =XSD.double)))

# Loop through CSV GDP and add triples
gdp["country"] = gdp["country"].apply(normalize_country_name)
for _,row in gdp.iterrows():
    country_name = row["country"].replace(" ", "_").replace(",", "")
    if country_name in valid_countries:
        country_uri = URIRef(EX + country_name)
        economy_uri = URIRef(EX + country_name + "_Economy")
        g.add((economy_uri, EX.hasEconomy, economy_uri))
        
        # Adding GDP
        g.add((economy_uri, DP.grossDomesticProduct, Literal(row["gdp"], datatype = XSD.double)))


# Loop through csv life expectancy + convertion to doubles (were strings before)
lifeExp["Health Expenditure %"] = pd.to_numeric(lifeExp["Health Expenditure %"], errors="coerce")
lifeExp["Education Expenditure %"] = pd.to_numeric(lifeExp["Education Expenditure %"], errors="coerce")
lifeExp["Corruption"] = pd.to_numeric(lifeExp["Corruption"], errors="coerce")
lifeExp["Country Name"] = lifeExp["Country Name"].apply(normalize_country_name)
for _,row in lifeExp.iterrows():
    country_name = row["Country Name"].replace(" ", "_").replace(",", "")
    if country_name in valid_countries:
        country_uri = URIRef(EX + country_name)
        economy_uri = URIRef(EX + country_name + "_Economy")
        g.add((economy_uri, EX.hasEconomy, economy_uri))

        # Adding Health Expenditure, Education Expenditure and Corruption 
        g.add((economy_uri, EX.exependitureOnHealth, Literal(row["Health Expenditure %"], datatype = XSD.double)))
        g.add((economy_uri, EX.exependitureOnEducation, Literal(row["Education Expenditure %"], datatype = XSD.double)))
        g.add((economy_uri, ISO3["11.4"] , Literal(row["Corruption"], datatype = XSD.double)))


# Loop trough CSV agriculture sector
agri["Country Name"] = agri["Country Name"].apply(normalize_country_name)
for _, row in agri.iterrows():
    country_name = row["Country Name"].replace(" ", "_").replace(",", "")
    if country_name in valid_countries:
        country_uri = URIRef(EX + country_name)
        sector_uri = URIRef(EX + country_name + "_Sector")
        g.add((sector_uri, RDF.type, EX.Sector))
        g.add((country_uri, EX.hasSector, sector_uri))  # Link to country

        # Adding Industry Rate
        g.add((sector_uri, EX.agricultureRate, Literal(row["2023"], datatype = XSD.double)))     


# Loop trough CSV industry sector
indu["Country Name"] = indu["Country Name"].apply(normalize_country_name)
for _, row in indu.iterrows():
    country_name = row["Country Name"].replace(" ", "_").replace(",", "")
    if country_name in valid_countries:
        country_uri = URIRef(EX + country_name)
        sector_uri = URIRef(EX + country_name + "_Sector")
        g.add((sector_uri, RDF.type, EX.Sector))
        g.add((country_uri, EX.hasSector, sector_uri))  # Link to country

        # Adding Industry Rate
        g.add((sector_uri, EX.industryeRate, Literal(row["2023"], datatype = XSD.double))) 


# Loop trough CSV service sector
serv["Country Name"] = serv["Country Name"].apply(normalize_country_name)
for _, row in serv.iterrows():
    country_name = row["Country Name"].replace(" ", "_").replace(",", "")
    if country_name in valid_countries:
        country_uri = URIRef(EX + country_name)
        sector_uri = URIRef(EX + country_name + "_Sector")
        g.add((sector_uri, RDF.type, EX.Sector))
        g.add((country_uri, EX.hasSector, sector_uri))  # Link to country

        # Adding Industry Rate
        g.add((sector_uri, EX.serviceRate, Literal(row["2023"], datatype = XSD.double)))        


# Loop through the CSV Population
popu["Country Name"] = popu["Country Name"].apply(normalize_country_name)
for _, row in popu.iterrows():
    country_name = row["Country Name"].replace(",", "").replace(" ", "_")
    if country_name in valid_countries:
        country_uri = URIRef(EX + country_name)   

        # Adding population information
        population_uri = URIRef(EX + country_name + "_Population")
        g.add((population_uri, RDF.type, EX.Population))
        g.add((country_uri, EX.hasPopulation, population_uri))  # Link it to the country
        g.add((population_uri, EX.hasPopulationSize, Literal(row.loc["Population, total [SP.POP.TOTL]"], datatype = XSD.int)))
        g.add((population_uri, EX.hasPopulationMaleSize, Literal(row.loc["Population, male (% of total population) [SP.POP.TOTL.MA.ZS]"], datatype = XSD.double)))
        g.add((population_uri, EX.hasPopulationFemaleSize, Literal(row.loc["Population, female (% of total population) [SP.POP.TOTL.FE.ZS]"], datatype = XSD.double)))  
        
        school_pop_uri = URIRef(EX + country_name + "_SchoolPopulation")
        g.add((school_pop_uri, RDF.type, EX.SchoolPopulation))
        g.add((country_uri, EX.hasSchoolPopulationData, school_pop_uri))  # Link to country                              
        g.add((school_pop_uri, EX.hasSchoolPopulation, Literal(row.loc["Population ages 0-14, total [SP.POP.0014.TO]"], datatype = XSD.double)))
        g.add((school_pop_uri, EX.hasSchoolMalePopulation, Literal(row.loc["Population, male (% of population, ages 0-14)"], datatype = XSD.double)))
        g.add((school_pop_uri, EX.hasSchoolFemalePopulation, Literal(row.loc["Population, female (% of population, ages 0-14)"], datatype = XSD.double)))

# Save the updated RDF graph
output_ttl = "New triplified data.ttl"
g.serialize(destination=output_ttl, format="turtle")

print(f"Updated RDF data saved to {output_ttl}")
