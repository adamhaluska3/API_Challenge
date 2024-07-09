from rest_framework.request import Request
from rest_framework.pagination import LimitOffsetPagination

from typing import List, Dict, Any

from .models import Country


defaultPaginationLimit: int = 50

class CountriesPaginator(LimitOffsetPagination):
    """
    Custom paginator based on native LimitOffsetPaginator. 
    
    Provides:
        URLs for next/previous request,
        pagination data (counter, offset and limit).    
    """
    
    
    def handleParameters(self, request: Request, countriesData: List[Country]) -> None:
        """
        Validates and sets all pagination parameters for correct pagination functioning.

        Args:
            request (Request): HTTP Request
            countriesData (List[Country]): List of Country entities to paginate.

        Returns:
            None
        """
        
        self.request = request
        
        self.count = len(countriesData)
        self.offset = int(request.query_params.get("offset", "0"))
        
        limit = request.query_params.get("limit")
        self.limit = int(limit) if (limit is not None) else defaultPaginationLimit
        
        request.query_params._mutable=True
        request.query_params["offset"] = self.offset
        request.query_params["limit"] = self.limit


    def getpaginatedData(self, request: Request, countriesData: List[Country]) -> Dict[str, Any]:
        """
        Paginates the ``countriesData`` using the values in ``request``.

        Parameters:
            request (Request): HTTP request.
            countriesData (List[Country]): List of countries to be used as pagination source.

        Returns:
            Dict[str, Any]: Dictionary containing prepared data for serialization of Countries object.
        """
        
        # Values required for 'paginate_queryset' to be set.
        self.handleParameters(request, countriesData)
        
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