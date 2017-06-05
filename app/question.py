from row_data_gateway.finder import BaseFinder
from row_data_gateway.gateway import BaseGateway


class Question(BaseGateway):
    _table_name = 'question'
    # Жестко задаем поля
    id = None
    text = None
    student_id = None

class QuestionFinder(BaseFinder):
    gateway = Question


