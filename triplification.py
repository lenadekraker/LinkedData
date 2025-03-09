from rdflib import Graph, Namespace, RDF, RDFS , XSD


EX = Namespace("http://example.org/educationOntology#")
GN = Namespace("http://www.geonames.org/ontology#")
DPV = Namespace("https://w3id.org/dpv#")
UNESCO = Namespace("http://www.unesco.org/ns/education#")
GEOP = Namespace("http://aims.fao.org/aos/geopolitical.owl#")
DBPEDIAOWL = Namespace("http://dbpedia.org/ontology/")
ISO37120 = Namespace("http://ontology.eil.utoronto.ca/ISO37120.owl#")

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
with open ("Global_Education.csv", 'r', encoding ='utf-8') as csvfile:
    g.add((EX.Country, RDF.type, GN.Class))

    # Geonames ontology
    g.add((EX.Country, RDFS.subClassOf, GN.Country))
    g.add((EX.Country, GN.lat, XSD.decimal))
    g.add((EX.Country, GN.long, XSD.decimal))
    g.add((EX.Continent, GN.lat, XSD.decimal))
    g.add((EX.Continent, GN.long, XSD.decimal))

    g.add((EX.GeographicalLocation, RDF.type, RDFS.Class))
    g.add((EX.EducationMetric, RDF.type, RDFS.Class))
    g.add((EX.Population, RDF.type, g.add((EX.Population, RDFS.subClassOf, DBPEDIAOWL.Population))))
    g.add((EX.FemalePopulation, RDF.type, RDFS.Class))
    g.add((EX.MalePopulation, RDF.type, RDFS.Class))
    g.add((EX.EconomicIndicatorGDP, RDF.type, RDFS.Class))
#--------------------------------------------------

g.add((EX.FemalePopulation, RDFS.subClassOf, EX.Population))
g.add((EX.MalePopulation, RDFS.subClassOf, EX.Population))

g.add((EX.hasGeographicalLocation , RDF.type, RDF.Property))
g.add((EX.hasGeographicalLocation, RDFS.domain, EX.Country))
g.add((EX.hasGeographicalLocation, RDFS.range, EX.GeographicalLocation))

g.add((EX.hasPopulation , RDF.type, RDF.Property))
g.add((EX.hasPopulation, RDFS.domain, EX.Country))
g.add((EX.hasPopulation, RDFS.range, EX.Population))

g.add((EX.hasLatitude, RDF.type, RDF.Property))
g.add((EX.hasLatitude, RDFS.domain, EX.GeographicalLocation))
g.add((EX.hasLatitude, RDFS.range, XSD.decimal))

g.add((EX.hasLongitude, RDF.type, RDF.Property))
g.add((EX.hasLongitude, RDFS.domain, EX.GeographicalLocation))
g.add((EX.hasLongitude, RDFS.range, XSD.decimal))

g.add((EX.hasEducationalMetric, RDF.type, RDF.Property))
g.add((EX.hasEducationalMetric, RDFS.domain, EX.Country))   
g.add((EX.hasEducationalMetric, RDFS.range, EX.EducationMetrics)) 

g.add((EX.hasOutOfSchoolRatePrePrimary, RDFS.subPropertyOf, EX.hasEducationalMetric))  
g.add((EX.hasOutOfSchoolRatePrimary,    RDFS.subPropertyOf, EX.hasEducationalMetric)) 
g.add((EX.hasOutOfSchoolRateLowerSecodary, RDFS.subPropertyOf, EX.hasEducationalMetric))  
g.add((EX.hasOutOfSchoolRateUpperSecodary, RDFS.subPropertyOf, EX.hasEducationalMetric)) 
g.add((EX.hasCompletionRatePrimary, RDFS.subPropertyOf, EX.hasEducationalMetric)) 
g.add((EX.hasCompletionRateLowerSecondary, RDFS.subPropertyOf, EX.hasEducationalMetric)) 
g.add((EX.hasCompletionRateUpperSecondary, RDFS.subPropertyOf, EX.hasEducationalMetric)) 
g.add((EX.hasLiteracyRateAmong15_24, RDFS.subPropertyOf, EX.hasEducationalMetric)) 
g.add((EX.hasGrossTertiaryEnrollment, RDFS.subPropertyOf, EX.hasEducationalMetric)) 
g.add((EX.hasGrossPrimaryEnrollment, RDFS.subPropertyOf, EX.hasEducationalMetric)) 
g.add((EX.hasHealthcareExpenditureGDP, RDFS.subPropertyOf, EX.hasEconomicIndicatorGDP))
g.add((EX.hasEducationExpenditureGDP, RDFS.subPropertyOf, EX.hasEconomicIndicatorGDP))
#------------------------------------------------------------------------

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

