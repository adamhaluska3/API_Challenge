# Development journal
## Planning phase
- My first encounter with API pagination. This concept will probably take some time to come up with some acceptable solution.

## Development phase
- For the sake of time-efficiency, the API project will is done in default Django Rest Framework (DRF) project template.
- **Country & CountryCreate**: Data from both classes are stored under single entry in _*Country*_ table of database (DB). This allows easier modification of response's format, and saves space compared to using two tables connected with foreign-key.
- **Utility models**: _*Links*_, _*Pagination*_, _*CollectionResult*_ and _*CountryCreate*_ models are created ad-hoc for each API request, so there's no need to store them in DB.