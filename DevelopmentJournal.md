# Development journal
## Planning phase
- My first encounter with API pagination. This concept will probably take some time to come up with some acceptable solution.

## Development phase
- For the sake of time-efficiency, the API project will is done in default Django Rest Framework (DRF) project template.

- **Country & CountryCreate**: Data from both classes are stored under single entry in _*Country*_ table of database (DB). This allows easier modification of response's format, and saves space compared to using two tables connected with foreign-key.

- **Utility models**: _*Links*_, _*Pagination*_, _*CollectionResult*_ and _*CountryCreate*_ models are created ad-hoc for each API request, so there's no need to store them in DB. (Update: utility models were completely removed, everything has been handled via nested Serializers.)

- **CountryPaginator**: Default LimitOffsetPaginator works as intended, but (AFAIK) it does not provide native ability to display fields 'next', 'previous' and others that were required in the response. That's why the custom _*CountriesPaginator*_ was needed. One issue I encountered is the non-working pagination,  due to custom names of offset and limit. (this was easily fixed by setting Pagination's parameters).

- **Default** _**PageLimit**_: set to 50 according to App.yaml file. This value is declared at the start of _*countriesPaginator.py*_ file (There are not enough 'hard-set' values for a reasonable creation of a separate file for constaints).

- **App.yaml imperfections**: File has a couple of issues:
    -  _*#/components/parameters/PageOffset*_ missed *required* field,
    - _*/countries/<id: int> response '404'*_ uses word 'Organization" instead of "Country".

- **Tests**: Even though I thoroughly tested the API using Postman, I wrote a couple of tests in _*tests.py*_ file.

- _**groupId**_ **usage**: Assignment did not specify the importance of _*groupId*_ parameter. By default, I set every new country's _*groupId*_ to 1. \
The project is ready for additional changes related to usage of _*groupId*_.

## Documentation phase
- **Purge of assignment files**: Before setting repo to public, assignment files had to be removed from repo and its history - ```git filter-repo``` and ```git push --force``` were used. \
Unfortunately, merge commit from branch _*api-implementation*_ to _*main*_ got lost (I suspect I forgot to pull Merge commit before I push-forced new changes).

- **Installation manual - OS**: Even though I developed this project on Windows, I included the manual for Linux as well, for the sake of usability.