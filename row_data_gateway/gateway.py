from collections import OrderedDict

from db import db


class BaseGateway(object):
    """
    Интерфейс для стандартного Gateway
    """
    # Служебное поле
    _table_name = None

    def __init__(self, *args, **kwargs):
        """
        Заполняем шлюз данными
        :param kwargs:
        """
        if args:
            for i, attr in enumerate(self.__class__.get_fields()):
                setattr(self, attr, args[i])
        if kwargs:
            for attr in self.__class__.get_fields():
                setattr(self, attr, kwargs[attr])

    @classmethod
    def get_fields(cls):
        """
        Поскольку в этом паттерне нет маппинга полей, а так же не должно быть никакой логики,
        то все поля, не являющиеся функциями и служебными полями, пытаемся записать в базу
        :return:
        """
        return [attr for attr, value in cls.__dict__.items() if not callable(value) and not attr.startswith('_')]

    def get_row_data(self):
        """
        Забираем из объекта поля, и подготавливаем для sql запроса
        :return:
        """
        data = OrderedDict()
        for attr in self.get_fields():
            data[attr] = getattr(self, attr)
        return data

    def __replace_or_insert(self, method):
        fields = ', '.format(self.get_fields())
        values = ':' + ', :'.join(self.get_row_data().keys())
        sql = "{method} INTO {table_name} {fields} VALUES {values}"
        sql = sql.format(method=method, table_name=self._table_name, fields=fields, values=values)
        db.execute(sql, self.get_row_data())

    def insert(self):
        self.__replace_or_insert('INSERT')

    def update(self):
        self.__replace_or_insert('REPLACE')
