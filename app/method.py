from row_data_gateway.finder import BaseFinder
from row_data_gateway.gateway import BaseGateway


class Method(BaseGateway):
    _table_name = 'method'
    # Жестко задаем поля
    id = None
    title = None
    link = None


class MethodMaterial(BaseFinder):
    gateway = Method


