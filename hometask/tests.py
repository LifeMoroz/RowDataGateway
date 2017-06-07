from unittest import TestCase

from django.test import Client
from django.urls import reverse
from mock import mock

from app.question import QuestionFinder, Question
import db

class TestQLogic(TestCase):

    def test_q_add(self):
        c = Client()
        resp = c.get(reverse('ask_view'))
        self.assertEqual(resp.status_code, 200)

    def test_q_finder(self):
        class X:
            def fetchall(self):
                return (1, '1234', 1),

        with mock.patch('db.db.execute', return_value=X()) as m:
            finder = QuestionFinder()
            obj = finder.find()[0]
            self.assertIsInstance(obj, finder.gateway)
            self.assertEqual(obj.text, '1234')
            self.assertEqual(obj.id, 1)
        m.assert_called_once()

    def test_q_gateway(self):
        with mock.patch('db.db.execute') as m:
            q = Question(1, "TestQ", 1)
            q.insert()
        m.assert_called_once()
