from rest_framework.pagination import PageNumberPagination


class MenuUserPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 1


class MessagePagination(PageNumberPagination):
    page_size = 35
    page_size_query_param = 'page_size'
    max_page_size = 1
