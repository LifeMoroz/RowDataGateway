from row_data_gateway.finder import BaseFinder
from row_data_gateway.gateway import BaseGateway


class Student(BaseGateway):
    _table_name = 'students'
    # Жестко задаем поля
    id = None
    first_name = None
    last_name = None
    password = None


class UserFinder(BaseFinder):
    gateway = Student


