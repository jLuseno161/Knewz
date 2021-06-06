import unittest
from app.models import Articles



class ArticleTest(unittest.TestCase):
    '''
    Test class to test articles
    '''
    def setUp(self):
        self.new_article = Articles(
            1234, 'Karls Aden', 'mytitle', 'mydescription', 'url','myimage','datecreated')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))
