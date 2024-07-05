# Development journal
## Planning phase
- My first encounter with API pagination. This concept will probably take some time to come up with some acceptable solution.

## Development phase
- For the sake of time-efficiency, the API project will is done in default Django Rest Framework (**DRF**) project template.
- **Country -> CountryCreated relation**: 'on_delete' set ot CASCADE - no need to perserve 'CountryCreated' when 'Country' gets deleted.
- **Utility models** - Links, Pagination and CollectionResult models are created ad-hoc for each API request, so there's no need to store them in DB.