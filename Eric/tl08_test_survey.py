import unittest
from tl08_survey import AnonymousSurvey

class TestAnonmousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question='What language did you first learn to speak'
        my_survey=AnonymousSurvey(question)
        my_survey.store_response('english')
        self.assertIn('English',my_survey.responses)
    def test_store_three_responses(self):
        question='What language did you first learn to speak'
        my_survey=AnonymousSurvey(question)
        responses=['english','chinese','french']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response.title(),my_survey.responses)

unittest.main()