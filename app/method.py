from db import db
from row_data_gateway.finder import BaseFinder
from row_data_gateway.gateway import BaseGateway


class Method(BaseGateway):
    _table_name = 'method'
    # Жестко задаем поля
    id = None
    title = None
    link = None


class MethodFinder(BaseFinder):
    gateway = Method

    @staticmethod
    def find_by_title_part(part):
        fields = ', '.join(MethodFinder.gateway.get_fields())
        sql = "SELECT {fields} FROM method WHERE title like ?".format(fields=fields)
        result = []
        for row in db.execute(sql, ['%' + part + '%']).fetchall():
            result.append(Method(*row))
        return result
