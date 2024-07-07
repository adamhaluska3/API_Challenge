from rest_framework.pagination import LimitOffsetPagination

class CountriesPaginator(LimitOffsetPagination):
    limit_query_param = "PageLimit"
    offset_query_param = "PageOffset"
        
    def getpaginatedData(self, request, countriesData):
        self.request = request
        
        self.count = len(countriesData)
        self.offset = int(request.query_params.get("PageOffset", "0"))
        
        limit = request.query_params.get("PageLimit")
        self.limit = int(limit) if (limit is not None) else 20
        
        links = {
            "previous": self.get_previous_link(),
            "next": self.get_next_link()
        }
        
        pagination = {
            "count": self.count,
            "offset": self.offset,
            "limit": self.limit
        }
        
        return {
            "links": links,
            "pagination": pagination,
            "countries": self.paginate_queryset(countriesData, request)
        }