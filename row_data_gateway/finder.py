from db import db


class BaseFinder(object):
    """
    стандартный Finder
    """
    gateway = None

    @classmethod
    def find(cls, **kwargs):
        where = ''
        data = []
        for key, value in kwargs.items():
            if where:
                where += ' and '
            else:
                where = 'WHERE '
            where += '{}=?'.format(key)
            data.append(value)
        fields = ', '.join(cls.gateway.get_fields())
        sql = "SELECT {fields} FROM {table_name} {where}".format(fields=fields, table_name=cls.gateway._table_name, where=where)
        result = []
        for row in db.execute(sql, data).fetchall():
            result.append(cls.gateway(*row))
        return result
