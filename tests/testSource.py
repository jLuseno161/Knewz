import unittest
from app.models import Sources


class SourceTest(unittest.TestCase):
    """Test source class"""

    def setUp(self):
        self.new_article = Sources(
            1234, 'Karls Aden', 'mydescription', 'url', 'mycategory', 'mycountry', 'mylanguage')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Sources))
