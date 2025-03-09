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


#remove all of this
g.add((EX.hasOutOfSchoolRatePrePrimary, RDF.type, RDF.Property)) 
g.add((EX.hasOutOfSchoolRatePrePrimary, RDFS.domain, EX.Population))   
g.add((EX.hasOutOfSchoolRatePrePrimary, RDFS.range, XSD.decimal))  

g.add((EX.hasOutOfSchoolRatePrimary, RDF.type, RDF.Property))  
g.add((EX.hasOutOfSchoolRatePrimary, RDFS.domain, EX.Population))   
g.add((EX.hasOutOfSchoolRatePrimary, RDFS.range, XSD.decimal))  

g.add((EX.hasOutOfSchoolRateLowerSecodary, RDF.type, RDF.Property))  
g.add((EX.hasOutOfSchoolRateLowerSecodary, RDFS.domain, EX.Population))   
g.add((EX.hasOutOfSchoolRateLowerSecodary, RDFS.range, XSD.decimal))

g.add((EX.hasOutOfSchoolRateUpperSecodary, RDF.type, RDF.Property))  
g.add((EX.hasOutOfSchoolRateUpperSecodary, RDFS.domain, EX.Population))  
g.add((EX.hasOutOfSchoolRateUpperSecodary, RDFS.range, XSD.decimal))

g.add((EX.hasCompletionRatePrimary, RDF.type, RDF.Property))  
g.add((EX.hasCompletionRatePrimary, RDFS.domain, EX.Population))  
g.add((EX.hasCompletionRatePrimary, RDFS.range, XSD.decimal))

g.add((EX.hasCompletionRateLowerSecondary, RDF.type, RDF.Property))  
g.add((EX.hasCompletionRateLowerSecondary, RDFS.domain, EX.Population))  
g.add((EX.hasCompletionRateLowerSecondary, RDFS.range, XSD.decimal))

g.add((EX.hasCompletionRateUpperSecondary, RDF.type, RDF.Property))  
g.add((EX.hasCompletionRateUpperSecondary, RDFS.domain, EX.Population))  
g.add((EX.hasCompletionRateUpperSecondary, RDFS.range, XSD.decimal))

g.add((EX.hasLiteracyRateAmong15_24, RDF.type, RDF.Property))
g.add((EX.hasLiteracyRateAmong15_24, RDFS.domain, EX.Population))
g.add((EX.hasLiteracyRateAmong15_24, RDFS.range, XSD.decimal))

g.add((EX.hasGrossTertiaryEnrollment, RDF.type, RDF.Property))  
g.add((EX.hasGrossTertiaryEnrollment, RDFS.domain, EX.Country))  
g.add((EX.hasGrossTertiaryEnrollment, RDFS.range, XSD.decimal))

g.add((EX.hasGrossPrimaryEnrollment, RDF.type, RDF.Property))  
g.add((EX.hasGrossPrimaryEnrollment, RDFS.domain, EX.Country))  
g.add((EX.hasGrossPrimaryEnrollment, RDFS.range, XSD.decimal))

g.add((EX.hasUnemploymentRate, RDF.type, RDF.Property))
g.add((EX.hasUnemploymentRate, RDFS.domain, EX.Country))
g.add((EX.hasUnemploymentRate, RDFS.range, XSD.decimal))


#just added this
g.add((EX.hasCorruptionRate, RDF.type, RDF.Property))
g.add((EX.hasCorruptionRate, RDFS.domain, EX.Country))
g.add((EX.hasCorruptionRate, RDFS.range, XSD.decimal))

#------------------------------------------------------------------------

g.add((EX.hasGDP, RDF.type, RDF.Property))  
g.add((EX.hasGDP, RDFS.domain, EX.Country))  
g.add((EX.hasGDP, RDFS.range, XSD.decimal))

g.add((EX.hasGDPpercent, RDF.type,    RDF.Property))  
g.add((EX.hasGDPpercent, RDFS.domain, EX.Country))  
g.add((EX.hasGDPpercent, RDFS.range, XSD.decimal))

g.add((EX.belongsTo, RDF.type,    RDF.Property))  
g.add((EX.belongsTo, RDFS.domain, EX.Country))  
g.add((EX.belongsTo, RDFS.range, EX.Continent))

g.add((EX.IncomeClass, RDF.type, RDFS.Class))
g.add((EX.hasIncomeClass, RDF.type, RDF.Property))
g.add((EX.hasIncomeClass, RDFS.domain, EX.Country))
g.add((EX.hasIncomeClass, RDFS.range, EX.IncomeClass))

g.add((EX.HighIncome, RDF.type, EX.IncomeClass))
g.add((EX.LowIncome, RDF.type, EX.IncomeClass))
g.add((EX.OtherIncome, RDF.type, EX.IncomeClass))

g.add((EX.hasEconomicIndicatorGDP, RDF.type, RDF.Property))
g.add((EX.hasEconomicIndicatorGDP, RDFS.domain, EX.Country))
g.add((EX.hasEconomicIndicatorGDP, RDFS.range,  EX.EconomicIndicatorGDP))

g.add((EX.HealthcareExpenditureGDP, RDF.type,  EX.EconomicIndicatorGDP))
g.add((EX.EducationExpenditureGDP,  RDF.type,  EX.EconomicIndicatorGDP))

g.add((EX.hasHealthcareExpenditureGDP, RDF.type, RDF.Property))
g.add((EX.hasHealthcareExpenditureGDP, RDFS.domain, EX.Country))
g.add((EX.hasHealthcareExpenditureGDP, RDFS.range,  XSD.decimal))

g.add((EX.hasEducationExpenditureGDP, RDF.type, RDF.Property))
g.add((EX.hasEducationExpenditureGDP, RDFS.domain, EX.Country))
g.add((EX.hasEducationExpenditureGDP, RDFS.range,  XSD.decimal))

g.add((EX.hasUndernourishmentRate, RDF.type, RDF.Property))
g.add((EX.hasUndernourishmentRate, RDFS.domain, EX.Country))
g.add((EX.hasUndernourishmentRate, RDFS.range, XSD.decimal))

#---------------------------------------------------------------------------------------------------
g.add((EX.hasAgricultureSectorRate, RDF.type, RDF.Property))
g.add((EX.hasAgricultureSectorRate, RDFS.domain, EX.Population))
g.add((EX.hasAgricultureSectorRate, RDFS.range, XSD.decimal))

g.add((EX.hasIndustrySectorRate, RDF.type, RDF.Property))
g.add((EX.hasIndustrySectorRate, RDFS.domain, EX.Population))
g.add((EX.hasIndustrySectorRate, RDFS.range, XSD.decimal))

g.add((EX.hasServiceSectorRate, RDF.type, RDF.Property))
g.add((EX.hasServiceSectorRate, RDFS.domain, EX.Population))
g.add((EX.hasServiceSectorRate, RDFS.range, XSD.decimal))

#_------------------------------------------------------------------------------------------------------------




with open("ontology.ttl", "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))

