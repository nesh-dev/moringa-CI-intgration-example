from django.test import TestCase
from .models import Tag

# Create your tests here.
class TagTestClass(TestCase): 

    def setUp(self): 
        self.tag =  Tag(name='job')

    def test_instance(self): 
        self.assertTrue(isinstance(self.tag, Tag))
    
