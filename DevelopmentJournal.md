# Development journal
## Planning phase
- My first encounter with API pagination. This concept will probably take some time to come up with some acceptable solution.

## Development phase
- For the sake of time-efficiency, the API project will is done in default Django Rest Framework (DRF) project template.

- **Country & CountryCreate**: Data from both classes are stored under single entry in _*Country*_ table of database (DB). This allows easier modification of response's format, and saves space compared to using two tables connected with foreign-key.

- **Utility models**: _*Links*_, _*Pagination*_, _*CollectionResult*_ and _*CountryCreate*_ models are created ad-hoc for each API request, so there's no need to store them in DB. (Update: utility models were completely removed, everything has been handled via nested Serializers.)

- **CountryPaginator**: Default LimitOffsetPaginator works as intended, but (AFAIK) it does not provide native ability to display fields 'next', 'previous' and others that were required in the response. That's why the custom _*CountriesPaginator*_ was needed.

- **Default** _**PageLimit**_: set to 50 according to App.yaml file. This value is declared at the start of _*countriesPaginator.py*_ file (There is not enough 'hard-set' values for a reasonable creation of a separate file for constaints).

- **App.yaml imperfections**: Extra parameters were not that much of an issue, but some parameters missed some fields (_*#/components/parameters/PageOffset*_ missed *required* field)