from rest_framework.request import Request
from rest_framework.pagination import LimitOffsetPagination

from typing import List, Dict, Any

from .models import Country


defaultPaginationLimit: int = 50  # TODO move ot constants?

class CountriesPaginator(LimitOffsetPagination):
    """
    Custom paginator based on native LimitOffsetPaginator. 
    
    Provides:
        URLs for next/previous request,
        pagination data (countr, offset and limit).    
    """
    limit_query_param = "PageLimit"
    offset_query_param = "PageOffset"


    def getpaginatedData(self, request: Request, countriesData: List[Country]) -> Dict[str:Any]:
        """
        Paginates the ``countriesData`` using the values in ``request``.

        Parameters:
            request (Request): HTTP request.
            countriesData (List[Country]): List of countries to be used as pagination source.

        Returns:
            Dict[str:Any]: Dictionary containing prepared data for serialization of Countries object.
        """
        
        # Values required for 'paginate_queryset' to be set.
        self.request = request
        
        self.count = len(countriesData)
        self.offset = int(request.query_params.get("PageOffset", "0"))
        
        limit = request.query_params.get("PageLimit")
        self.limit = int(limit) if (limit is not None) else defaultPaginationLimit
        
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