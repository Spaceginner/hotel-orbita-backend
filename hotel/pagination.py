from rest_framework import pagination
from rest_framework.response import Response


class SimplePagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'pages': self.page.paginator.num_pages,
            'results': data,
        })

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'required': ['count', 'pages', 'results'],
            'properties': {
                'count': {
                    'type': 'integer',
                    'example': 123,
                },
                'pages': {
                    'type': 'integer',
                    'example': 12,
                },
                'results': schema,
            },
        }
