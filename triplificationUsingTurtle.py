from rdflib import Graph, URIRef, Literal, Namespace, RDF, XSD
import pandas as pd

# Loading in Turtle file, from Protégé
g = Graph()
g.parse("MainProject.ttl", format = "turtle")

# Loading in the data in different csv's
agri = pd.read_csv("agricultureSector.csv", delimiter=",", skiprows=4)
gdp = pd.read_csv("GDP.csv", delimiter=",")
gdp = gdp.drop_duplicates(subset="country", keep="last") # Keep only the last occurrence of each country
globalEdu = pd.read_csv("Global_Education.csv", delimiter=",", encoding="ISO-8859-1")
indu = pd.read_csv("industrySector.csv", delimiter=",", skiprows = 4)
lifeExp = pd.read_csv("life expectancy.csv", delimiter=",")
lifeExp = lifeExp.drop_duplicates(subset = "Country Name", keep = "last")
serv = pd.read_csv("serviceSector.csv", delimiter=",", skiprows = 4)

# Get namespaces from the ontology 
EX = Namespace("http://example.org/educationOntology#")
DBPEDIA = Namespace("http://dbpedia.org/")
GN = Namespace("http://www.geonames.org/ontology#")
ISO37210 = Namespace("http://ontology.eil.utoronto.ca/ISO37120.owl#")
DPV = Namespace("http://www.w3.org/ns/dpv#")
SCHEMA = Namespace("http://schema.org/")

# Bind namespaces to the graph
g.bind("ex", EX)
g.bind("dbpedia", DBPEDIA)
g.bind("gn", GN)
g.bind("iso37210", ISO37210)
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
    return country_name_corrections.get(name, name).replace(" ", "_").replace(",", "")


# Loop through CSV Global Education and add triples
globalEdu["Countries and areas"] = globalEdu["Countries and areas"].apply(normalize_country_name)
for _, row in globalEdu.iterrows():
    country_name = row["Countries and areas"].replace(" ", "_").replace(",", "") 
    country_uri = URIRef(EX + country_name)

    # Adding country, longitude and latitude
    g.add((country_uri, GN.name, Literal(row["Countries and areas"], datatype = XSD.string)))
    g.add((country_uri, GN.lat, Literal(row["Latitude "], datatype = XSD.double)))
    g.add((country_uri, GN.long, Literal(row["Longitude"], datatype = XSD.double)))
    g.add((country_uri, ISO37210["5.1"], Literal(row["Unemployment_Rate"], datatype=XSD.double)))


# Loop through CSV GDP and add triples
gdp["country"] = gdp["country"].apply(normalize_country_name)
for _,row in gdp.iterrows():
    country_name = row["country"].replace(" ", "_").replace(",", "")
    country_uri = URIRef(EX + country_name)
    
    # Adding GDP
    g.add((country_uri, DBPEDIA.grossDomesticProduct, Literal(row["gdp"], datatype = XSD.double)))


# Loop through csv life expectancy + convertion to doubles (were strings before)
lifeExp["Health Expenditure %"] = pd.to_numeric(lifeExp["Health Expenditure %"], errors="coerce")
lifeExp["Education Expenditure %"] = pd.to_numeric(lifeExp["Education Expenditure %"], errors="coerce")
lifeExp["Corruption"] = pd.to_numeric(lifeExp["Corruption"], errors="coerce")
lifeExp["Country Name"] = lifeExp["Country Name"].apply(normalize_country_name)
for _,row in lifeExp.iterrows():
    country_name = row["Country Name"].replace(" ", "_").replace(",", "")
    country_uri = URIRef(EX + country_name)

    # Adding Health Expenditure, Education Expenditure and Corruption 
    g.add((country_uri, EX.exependitureOnHealth, Literal(row["Health Expenditure %"], datatype = XSD.double)))
    g.add((country_uri, EX.exependitureOnEducation, Literal(row["Education Expenditure %"], datatype = XSD.double)))
    g.add((country_uri, ISO37210["11.4"] , Literal(row["Corruption"], datatype = XSD.double)))


# Loop trough CSV agriculture sector
agri["Country Name"] = agri["Country Name"].apply(normalize_country_name)
for _, row in agri.iterrows():
    country_name = row["Country Name"].replace(" ", "_").replace(",", "")
    country_uri = URIRef(EX + country_name)

    # Adding Industry Rate
    g.add((country_uri, EX.agricultureRate, Literal(row["2023"], datatype = XSD.double)))     


# Loop trough CSV industry sector
indu["Country Name"] = indu["Country Name"].apply(normalize_country_name)
for _, row in indu.iterrows():
    country_name = row["Country Name"].replace(" ", "_").replace(",", "")
    country_uri = URIRef(EX + country_name)

    # Adding Industry Rate
    g.add((country_uri, EX.industryeRate, Literal(row["2023"], datatype = XSD.double))) 


# Loop trough CSV service sector
serv["Country Name"] = serv["Country Name"].apply(normalize_country_name)
for _, row in serv.iterrows():
    country_name = row["Country Name"].replace(" ", "_").replace(",", "")
    country_uri = URIRef(EX + country_name)

    # Adding Industry Rate
    g.add((country_uri, EX.serviceRate, Literal(row["2023"], datatype = XSD.double)))                                           
    

# Save the updated RDF graph
output_ttl = "triplified data.ttl"
g.serialize(destination=output_ttl, format="turtle")

print(f"Updated RDF data saved to {output_ttl}")
