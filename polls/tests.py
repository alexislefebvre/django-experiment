# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone

from django.test import TestCase

from polls.models import Choice, Question

class QuestionTestCase(TestCase):
    def setUp(self):
        Question.objects.create(question_text="What's up?", pub_date=timezone.now())

    def test_question_text(self):
        """Question"""
        question = Question.objects.get(question_text="What's up?")
        self.assertEqual(question.question_text, 'What\'s up?')
