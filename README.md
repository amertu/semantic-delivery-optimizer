# Semantic Delivery Coordination Framework
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/amertu/semantic-delivery-optimizer/docker-build.yml?logo=github)

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.2.5-2a2929?logo=flask&logoColor=white)
![GraphDB](https://img.shields.io/badge/GraphDB-8.7-F05032?logo=graphdb&logoColor=white)
![SPARQL](https://img.shields.io/badge/SPARQL-E34F26?logo=rdf4j&logoColor=white)
![RDF4J](https://img.shields.io/badge/RDF4J-3.3.7-3776AB?logo=rdf4j&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter%20Notebook-%E2%9C%94-F37626?logo=jupyter&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-3.0-2496ED?logo=docker&logoColor=white)

## Project Overview
Developed a semantic framework to optimize order coordination across multiple delivery services, leveraging ontologies and knowledge graphs for intelligent data integration.

# Architecture
```markdown
                                  ┌───────────────────────────┐
                                  │       Web Browser         │
                                  └───────────┬───────────────┘
                                              │
                                 HTTP Request │ Result: JSON
                                              ▼
                                  ┌───────────────────────────┐
                                  │      Web Server           │
                                  │   [Docker Container]      │
                                  │                           │
                                  │    Python + Flask         │
                                  └───────────┬───────────────┘
                                              │
                          SPARQL HTTP Query   │ Result: JSON
                                              ▼
                                  ┌───────────────────────────┐
                                  │    RDF4J Workbench        │
                                  │   [Docker Container]      │
                                  │                           │
                                  │  Triplestore + UI + API   │
                                  └───────────────────────────┘

                     ┌─────────────────────────────────────────────────────┐
                     │      All containers connected via Docker network    │
                     └─────────────────────────────────────────────────────┘

```

## Key Features
- **Semantic Integration**: Designed and implemented an ontology-based system to unify data from 4+ delivery service providers.
- **Knowledge Graphs**: Utilized RDF and SPARQL to create a scalable and flexible knowledge graph for querying and reasoning.
- **System Architecture**: Deployed services using Docker to ensure modularity and scalability.

## Business Impact
- **Optimized Delivery Coordination**: Improved route planning and order synchronization, resulting in significantly reduced delivery times.
- **Enhanced Operational Efficiency**: Streamlined inter-system communication, leading to better service reliability and a superior user experience.





