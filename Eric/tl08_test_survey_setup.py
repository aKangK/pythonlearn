import unittest
from tl08_survey import AnonymousSurvey

class TestAnonmousSurvey(unittest.TestCase):
    def setUp(self):
        question='What language did you first learn to speak'
        self.my_survey=AnonymousSurvey(question)
        self.test_cases=['English','Chinese','French']
    def test_store_single_response(self):
        self.my_survey.store_response(self.test_cases[0])
        self.assertIn(self.test_cases[0],self.my_survey.responses)
    def test_store_many_responses(self):
        for response in self.test_cases:
            self.my_survey.store_response(response)
        for response in self.test_cases:
            self.assertIn(response.title(),self.my_survey.responses)

unittest.main()