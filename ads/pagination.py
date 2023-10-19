from rest_framework.pagination import PageNumberPagination


class BulletinBoardPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_size_query_param = 'page_size'
