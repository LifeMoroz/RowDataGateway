from row_data_gateway.finder import BaseFinder
from row_data_gateway.gateway import BaseGateway


class News(BaseGateway):
    _table_name = 'news'
    # Жестко задаем поля
    id = None
    title = None
    text = None


class NewsFinder(BaseFinder):
    gateway = News


