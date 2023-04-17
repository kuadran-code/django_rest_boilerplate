from rest_framework import pagination, response

class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return response.Response({
            'results': data,
            'meta': {
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'count': self.page.paginator.count,
                'pages': self.page.paginator.num_pages,
                'page': self.page.number,
                'per_page': self.page.paginator.per_page
            },
        })
