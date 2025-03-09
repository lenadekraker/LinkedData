from rdflib import Graph, Namespace, RDF, RDFS , XSD


EX = Namespace("http://example.org/ontology#")

EX = Namespace("http://example.org/educationOntology#")
GN = Namespace("http://www.geonames.org/ontology#")
GEO = Namespace("http://www.geonames.org/ontology#population")
DPV = Namespace("https://w3id.org/dpv#")
UNESCO = Namespace("http://www.unesco.org/ns/education#")
GEOP = Namespace("http://aims.fao.org/aos/geopolitical.owl#")
DBPEDIAOWL = Namespace("http://dbpedia.org/ontology/")
ISO37120 = Namespace("http://ontology.eil.utoronto.ca/ISO37120.owl#")
DBPEDIA = Namespace("http://dbpedia.org/ontology/")

g = Graph()
g.bind("ex", EX)
g.bind("gn", GN)
g.bind("geo", GEO)
g.bind("dpv", DPV)
g.bind("unesco", UNESCO)
g.bind("geop", GEOP)
g.bind("dbpediaOwl", DBPEDIAOWL)
g.bind("iso37120", ISO37120)
#---------------------------------------------


#here
g.add((GN.name, RDF.type, RDF.Property))
g.add((GN.name, RDFS.domain, GN.Country))
g.add((GN.name, RDFS.range, XSD.string))
g.add((DBPEDIA.Population, RDF.type, RDFS.Class))
g.add((DBPEDIAOWL.populationTotal, RDF.type, RDF.Property))
g.add((DBPEDIAOWL.populationTotal, RDFS.domain, DBPEDIA.Population))
g.add((DBPEDIAOWL.populationTotal, RDFS.range, XSD.int)) 
g.add((DBPEDIA.populationPctWomen, RDF.type, RDF.Property))
g.add((DBPEDIA.populationPctWomen, RDFS.domain, DBPEDIA.Population))
g.add((DBPEDIA.populationPctWomen, RDFS.range, XSD.double))  
g.add((DBPEDIA.populationPctMen, RDF.type, RDF.Property))
g.add((DBPEDIA.populationPctMen, RDFS.domain, DBPEDIA.Population))
g.add((DBPEDIA.populationPctMen, RDFS.range, XSD.double)) 
#--------------------------------------------------
g.add((UNESCO.CompletionRate, RDF.type, RDFS.Class))

g.add((UNESCO.completionRatePrimary, RDF.type, RDF.Property))
g.add((UNESCO.completionRatePrimary, RDFS.domain, UNESCO.CompletionRate))
g.add((UNESCO.completionRatePrimary, RDFS.range, XSD.int)) 
g.add((UNESCO.completionRateLowerSecondary, RDF.type, RDF.Property))
g.add((UNESCO.completionRateLowerSecondary, RDFS.domain, UNESCO.CompletionRate))
g.add((UNESCO.completionRateLowerSecondary, RDFS.range, XSD.int)) 
g.add((UNESCO.completionRateUpperSecondary, RDF.type, RDF.Property))
g.add((UNESCO.completionRateUpperSecondary, RDFS.domain, UNESCO.CompletionRate))
g.add((UNESCO.completionRateUpperSecondary, RDFS.range, XSD.int)) 
#------------------------------------------------------------------------

g.add((UNESCO.OutOfSchoolRate, RDF.type, RDFS.Class))
g.add((UNESCO.OutOfSchoolRatePrimary, RDF.type, RDF.Property))
g.add((UNESCO.OutOfSchoolRatePrimary, RDFS.domain, UNESCO.OutOfSchoolRate))
g.add((UNESCO.OutOfSchoolRatePrePrimary, RDFS.range, XSD.int)) 

g.add((UNESCO.OutOfSchoolRatePrePrimary, RDF.type, RDF.Property))
g.add((UNESCO.OutOfSchoolRatePrePrimary, RDFS.domain, UNESCO.OutOfSchoolRate))
g.add((UNESCO.OutOfSchoolRatePrePrimary, RDFS.range, XSD.int)) 

g.add((UNESCO.OutOfSchoolRateLowerSecondary, RDF.type, RDF.Property))
g.add((UNESCO.OutOfSchoolRateLowerSecondary, RDFS.domain, UNESCO.OutOfSchoolRate))
g.add((UNESCO.OutOfSchoolRateLowerSecondary, RDFS.range, XSD.int)) 

g.add((UNESCO.OutOfSchoolRateUpperSecondary, RDF.type, RDF.Property))
g.add((UNESCO.OutOfSchoolRateUpperSecondary, RDFS.domain, UNESCO.OutOfSchoolRate))
g.add((UNESCO.OutOfSchoolRateUpperSecondary, RDFS.range, XSD.int)) 
#--------------------------------------------------------------------

g.add((EX.hasAgricultureSectorRate, RDF.type, RDF.Property))
g.add((EX.hasAgricultureSectorRate, RDFS.domain, EX.Population))
g.add((EX.hasAgricultureSectorRate, RDFS.range, XSD.decimal))

g.add((EX.hasIndustrySectorRate, RDF.type, RDF.Property))
g.add((EX.hasIndustrySectorRate, RDFS.domain, EX.Population))
g.add((EX.hasIndustrySectorRate, RDFS.range, XSD.decimal))

g.add((EX.hasServiceSectorRate, RDF.type, RDF.Property))
g.add((EX.hasServiceSectorRate, RDFS.domain, EX.Population))
g.add((EX.hasServiceSectorRate, RDFS.range, XSD.decimal))

#------------------------------------------------------------------------
g.add((ISO37120.Economy, RDF.type, RDFS.Class))
g.add((ISO37120.EconomyIndicator_5_1, RDF.type, RDF.Property))
g.add((ISO37120.EconomyIndicator_5_1, RDFS.domain, ISO37120.Economy))
g.add((ISO37120.EconomyIndicator_5_1, RDFS.range, XSD.decimal))


g.add((EX.unemploymentRate, RDF.type, RDF.Property))
g.add((EX.unemploymentRate, RDFS.domain, ISO37120.Economy))
g.add((EX.unemploymentRate, RDFS.range, XSD.decimal))

g.add((EX.corruptionRate, RDF.type, RDF.Property))
g.add((EX.corruptionRate, RDFS.domain, ISO37120.Economy))
g.add((EX.corruptionRate, RDFS.range, XSD.decimal))

g.add((GEOP.GDP, RDF.type, RDF.Property))
g.add((GEOP.GDP, RDFS.domain, ISO37120.Economy))
g.add((GEOP.GDP, RDFS.range, XSD.decimal))

g.add((EX.expenditureOnHealth, RDF.type, RDF.Property))
g.add((EX.expenditureOnHealth, RDFS.domain, ISO37120.Economy))
g.add((EX.expenditureOnHealth, RDFS.range, XSD.decimal))

g.add((EX.expenditureOnEducation, RDF.type, RDF.Property))
g.add((EX.expenditureOnEducation, RDFS.domain, ISO37120.Economy))
g.add((EX.expenditureOnEducation, RDFS.range, XSD.decimal))
#_------------------------------------------------------------------------------------------------------------




with open("ontology.ttl", "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))

