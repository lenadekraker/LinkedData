from rdflib import Graph, Namespace, RDF, RDFS, Literal

# Define namespace
EX = Namespace("http://example.org/ontology#")

g = Graph()
g.bind("ex", EX)

# Define Classes
g.add((EX.Country, RDF.type, RDFS.Class))
g.add((EX.GeographicalLocation, RDF.type, RDFS.Class))
g.add((EX.EducationMetric, RDF.type, RDFS.Class))

# Define Properties
g.add((EX.hasLatitude, RDF.type, RDF.Property))
g.add((EX.hasLatitude, RDFS.domain, EX.Country))
g.add((EX.hasLatitude, RDFS.range, RDFS.Literal))

g.add((EX.hasLongitude, RDF.type, RDF.Property))
g.add((EX.hasLongitude, RDFS.domain, EX.Country))
g.add((EX.hasLongitude, RDFS.range, RDFS.Literal))

g.add((EX.hasOutOfSchoolRateMale, RDF.type, RDF.Property))
g.add((EX.hasOutOfSchoolRateMale, RDFS.domain, EX.Country))
g.add((EX.hasOutOfSchoolRateMale, RDFS.range, RDFS.Literal))

g.add((EX.hasOutOfSchoolRateFemale, RDF.type, RDF.Property))
g.add((EX.hasOutOfSchoolRateFemale, RDFS.domain, EX.Country))
g.add((EX.hasOutOfSchoolRateFemale, RDFS.range, RDFS.Literal))

# Serialize the graph in Turtle format and save to a file
g.serialize(destination="ontology.ttl", format="turtle")
