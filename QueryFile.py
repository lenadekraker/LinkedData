import requests
import json





query = """
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX geo: <http://www.geonames.org/ontology#> 
PREFIX ex: <http://example.org/educationOntology#>
PREFIX gn: <http://www.geonames.org/ontology#>
PREFIX schema: <http://schema.org/>
PREFIX sdo: <http://schema.org/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX db: <http://dbpedia.org/>
PREFIX iso3: <http://ontology.eil.utoronto.ca/ISO37120.owl#>

SELECT ?country ?corruption 
WHERE {
  {
    SELECT (AVG(xsd:double(?corruption)) AS ?avgCorruption)
    WHERE {
      ?country a schema:Country .
      ?country ex:hasEconomy ?economy_data .
      ?economy_data iso3:11.4 ?corruption.
      FILTER(isNumeric(?corruption))
      FILTER (?corruption != "NaN"^^xsd:double)  
    }
  }
  ?country a schema:Country .
  ?country ex:hasEconomy ?economy_data .
  ?economy_data iso3:11.4 ?corruption.
  FILTER(isNumeric(?corruption))
  FILTER (?corruption != "NaN"^^xsd:double)  
  FILTER (xsd:double(?corruption) > ?avgCorruption) 
}
ORDER BY ASC(?corruption)
"""

headers = {
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ1bmtub3duIiwiaXNzIjoiaHR0cHM6Ly9hcGkudHJpcGx5ZGIuY29tIiwianRpIjoiZmNlZjE4MGQtYWUxYS00ZWE3LTgxYzQtM2ZjMzE5MGI2MGQwIiwidWlkIjoiNjdjNTkzMzcxZWJhODg0ZDk2Y2JkMzc2IiwiaWF0IjoxNzQ0MTE0ODQ4fQ.eNyXtdFvA3rhTi4vMorrUhnyGCTnoIZUKWuRSeuNmiM',
    'Content-Type': 'application/json'
}

data = {
    "query": query
}
response = requests.get(url='https://api.triplydb.com/datasets/LenaKraker/ProjectLinkedDataSemanticWeb/sparql', headers=headers , json=data)


if response.status_code == 200:
    data = response.json()
    print(data)

else:
    print(f"Failed to retrieve data: {response.status_code}")
    print("Response content:", response.text) 


data = {
    "query": query
}

response = requests.post(url='https://api.triplydb.com/datasets/LenaKraker/ProjectLinkedDataSemanticWeb/sparql', headers=headers, json=data)


if response.status_code == 200:
    data = response.json()  
    print(data)
else:
    print(f"Failed to retrieve data: {response.status_code}")
    print("Response content:", response.text)