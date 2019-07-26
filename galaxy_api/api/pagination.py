from rest_framework import pagination
from rest_framework.response import Response
from rest_framework.utils.urls import remove_query_param, replace_query_param


class LimitOffsetPagination(pagination.LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

    def get_first_link(self):
        url = self.request.get_full_path()
        url = replace_query_param(url, self.limit_query_param, self.limit)

        return replace_query_param(url, self.offset_query_param, 0)

    def get_last_link(self):
        url = self.request.get_full_path()
        url = replace_query_param(url, self.limit_query_param, self.limit)

        offset = self.count - self.limit if (self.count - self.limit) >= 0 else 0
        return replace_query_param(url, self.offset_query_param, offset)

    def get_next_link(self):
        if self.offset + self.limit >= self.count:
            return None

        url = self.request.get_full_path()
        url = replace_query_param(url, self.limit_query_param, self.limit)

        offset = self.offset + self.limit
        return replace_query_param(url, self.offset_query_param, offset)

    def get_previous_link(self):
        if self.offset <= 0:
            return None

        url = self.request.get_full_path()
        url = replace_query_param(url, self.limit_query_param, self.limit)

        if self.offset - self.limit <= 0:
            return remove_query_param(url, self.offset_query_param)

        offset = self.offset - self.limit
        return replace_query_param(url, self.offset_query_param, offset)

    def get_paginated_response(self, data):
        return Response({
            'meta': {
                'count': self.count,
            },
            'links': {
                'first': self.get_first_link(),
                'previous': self.get_previous_link(),
                'next': self.get_next_link(),
                'last': self.get_last_link(),
            },
            'data': data,
        })
