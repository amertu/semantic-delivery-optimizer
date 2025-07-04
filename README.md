# Semantic Delivery Coordination Framework
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/amertu/semantic-delivery-optimizer/docker-build.yml?logo=github)

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.2.5-2a2929?logo=flask&logoColor=white)
![GraphDB](https://img.shields.io/badge/GraphDB-8.7-F05032?logo=graphdb&logoColor=white)
![SPARQL](https://img.shields.io/badge/SPARQL-1.1-E34F26?logo=rdf4j&logoColor=white)
![RDF4J](https://img.shields.io/badge/RDF4J-3.3.7-3776AB?logo=rdf4j&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter%20Notebook-%E2%9C%94-F37626?logo=jupyter&logoColor=white)
![OpenRefine](https://img.shields.io/badge/OpenRefine-3.9.3-blue.svg?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4NCjwhLS0gVXBsb2FkZWQgdG86IFNWRyBSZXBvLCB3d3cuc3ZncmVwby5jb20sIFRyYW5zZm9ybWVkIGJ5OiBTVkcgUmVwbyBNaXhlciBUb29scyAtLT4KPHN2ZyBmaWxsPSIjZmZmZmZmIiB3aWR0aD0iMjA5cHgiIGhlaWdodD0iMjA5cHgiIHZpZXdCb3g9IjAgMCAyNC4wMCAyNC4wMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMC4wMDAyNDAwMDAwMDAwMDAwMDAwMyI%2BCg08ZyBpZD0iU1ZHUmVwb19iZ0NhcnJpZXIiIHN0cm9rZS13aWR0aD0iMCIvPgoNPGcgaWQ9IlNWR1JlcG9fdHJhY2VyQ2FycmllciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIi8%2BCg08ZyBpZD0iU1ZHUmVwb19pY29uQ2FycmllciI%2BIDxwYXRoIGQ9Ik0xNy4wODk4LDguOTk5OSBMMTcuNzg0OCw0LjgyOTkgTDIwLjU2NTgsOC45OTk5IEwxNy4wODk4LDguOTk5OSBaIE0xNi44MzU4LDkuOTk5OSBMMjAuNDA2OCw5Ljk5OTkgTDEzLjYyMDgsMTcuODU3OSBMMTYuODM1OCw5Ljk5OTkgWiBNNy4xNjM4LDkuOTk5OSBMMTAuMzc4OCwxNy44NTc5IEwzLjU5MTgsOS45OTk5IEw3LjE2MzgsOS45OTk5IFogTTYuOTA5OCw4Ljk5OTkgTDMuNDMzOCw4Ljk5OTkgTDYuMjE0OCw0LjgyOTkgTDYuOTA5OCw4Ljk5OTkgWiBNNy44MDA4LDguMjY0OSBMNy4wODk4LDMuOTk5OSBMMTAuOTk5OCwzLjk5OTkgTDcuODAwOCw4LjI2NDkgWiBNMTIuOTk5OCwzLjk5OTkgTDE2LjkwOTgsMy45OTk5IEwxNi4xOTg4LDguMjY0OSBMMTIuOTk5OCwzLjk5OTkgWiBNOC40OTk4LDguOTk5OSBMMTEuOTk5OCw0LjMzMjkgTDE1LjQ5OTgsOC45OTk5IEw4LjQ5OTgsOC45OTk5IFogTTE1Ljc1NDgsOS45OTk5IEwxMS45OTk4LDE5LjE3OTkgTDguMjQ0OCw5Ljk5OTkgTDE1Ljc1NDgsOS45OTk5IFogTTIxLjkxNTgsOS4yMjI5IEwxNy45MTU4LDMuMjIyOSBDMTcuOTE0OCwzLjIyMDkgMTcuOTExOCwzLjIxOTkgMTcuOTEwOCwzLjIxNzkgQzE3Ljg2ODgsMy4xNTY5IDE3LjgxMzgsMy4xMDY5IDE3Ljc0NzgsMy4wNjk5IEMxNy43Mjg4LDMuMDU4OSAxNy43MDc4LDMuMDU1OSAxNy42ODg4LDMuMDQ2OSBDMTcuNjUyOCwzLjAzMjkgMTcuNjIwOCwzLjAxMjkgMTcuNTgxOCwzLjAwNjkgQzE3LjU2NTgsMy4wMDM5IDE3LjU0OTgsMy4wMDk5IDE3LjUzMjgsMy4wMDc5IEMxNy41MjE4LDMuMDA3OSAxNy41MTE4LDIuOTk5OSAxNy40OTk4LDIuOTk5OSBMNi40OTk4LDIuOTk5OSBDNi40ODc4LDIuOTk5OSA2LjQ3NzgsMy4wMDc5IDYuNDY1OCwzLjAwNzkgQzYuNDQ5OCwzLjAwOTkgNi40MzQ4LDMuMDAzOSA2LjQxNzgsMy4wMDY5IEM2LjM3ODgsMy4wMTI5IDYuMzQ2OCwzLjAzMjkgNi4zMTE4LDMuMDQ2OSBDNi4yOTE4LDMuMDU1OSA2LjI3MDgsMy4wNTg5IDYuMjUyOCwzLjA2OTkgQzYuMTg2OCwzLjEwNjkgNi4xMzA4LDMuMTU2OSA2LjA4OTgsMy4yMTc5IEM2LjA4NzgsMy4yMTk5IDYuMDg1OCwzLjIyMDkgNi4wODM4LDMuMjIyOSBMMi4wODM4LDkuMjIyOSBDMS45NTk4LDkuNDA5OSAxLjk3NDgsOS42NTY5IDIuMTIxOCw5LjgyNjkgTDExLjYyMTgsMjAuODI2OSBDMTEuNjQyOCwyMC44NTE5IDExLjY3MTgsMjAuODYyOSAxMS42OTY4LDIwLjg4MjkgQzExLjcxODgsMjAuODk5OSAxMS43Mzc4LDIwLjkxODkgMTEuNzYyOCwyMC45MzE5IEMxMS45MTE4LDIxLjAxMzkgMTIuMDg3OCwyMS4wMTM5IDEyLjIzNjgsMjAuOTMxOSBDMTIuMjYxOCwyMC45MTg5IDEyLjI4MDgsMjAuODk5OSAxMi4zMDI4LDIwLjg4MjkgQzEyLjMyNzgsMjAuODYyOSAxMi4zNTY4LDIwLjg1MTkgMTIuMzc4OCwyMC44MjY5IEwyMS44Nzg4LDkuODI2OSBDMjIuMDI1OCw5LjY1NjkgMjIuMDQwOCw5LjQwOTkgMjEuOTE1OCw5LjIyMjkgTDIxLjkxNTgsOS4yMjI5IFoiLz4gPC9nPgoNPC9zdmc%2B)
![Docker](https://img.shields.io/badge/Docker-3.0-2496ED?logo=docker&logoColor=white)

## Project Overview
Developed a semantic framework to optimize order coordination across multiple delivery services, leveraging ontologies and knowledge graphs for intelligent data integration.


## Key Features
- **Semantic Integration**: Designed and implemented an ontology-based system to unify data from 4+ delivery service providers.
- **Knowledge Graphs**: Utilized RDF and SPARQL to create a scalable and flexible knowledge graph for querying and reasoning.
- **System Architecture**: Deployed services using Docker to ensure modularity and scalability.
  
## Architecture
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

## Project Report

[The full report is available via Overleaf](https://www.overleaf.com/read/dpwcdbnybphd#585da5)



