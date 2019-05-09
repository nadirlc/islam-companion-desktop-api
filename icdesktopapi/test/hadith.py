import sys,os
import unittest
sys.path.append('..')

from hadith_api import Hadith_Api

class TestHadith_Api(unittest.TestCase):
    """Used to test the hadith api"""
 
    @classmethod
    def setUpClass(cls):
   
        # The absolute path to the database 
        cur_dir         = os.path.dirname(os.path.realpath(__file__))
        db_path         = os.path.abspath(cur_dir + "../data/hadith.db")
        
        """It creates an object of type Hadith_Api"""
        cls.hadith_api = Hadith_Api(db_path)
        
    def test_get_source_list(self):
        """It checks if the number of hadith sources fetched
        from database is 5
        """

        cls         = self.__class__
        source_list = cls.hadith_api.get_source_list()
        self.assertEqual(len(source_list), 5)

    def test_get_book_list(self):
        """It checks if the number of hadith books fetched
        from database is 5 for the source "صحیح بخاری"
        """
        
        cls       = self.__class__
        source    = "صحیح بخاری"
        book_list = cls.hadith_api.get_book_list(source)
        self.assertEqual(len(book_list), 95)
        
    def test_get_title_list(self):
        """It checks if the number of hadith titles fetched
        from database is 172 for the source "صحیح بخاری"
        and the book "انصار کے مناقب"
        """
        
        cls        = self.__class__
        source     = "صحیح بخاری"
        book       = "انصار کے مناقب"
        title_list = cls.hadith_api.get_title_list(source, book)
        self.assertEqual(len(title_list), 172)
        
    def test_get_hadith_text(self):
        """It checks if the length of hadith text for the
        hadith id 10 is 1412
        """
        
        cls         = self.__class__
        hadith_id   = 10
        hadith_text = cls.hadith_api.get_hadith_text(hadith_id)
        self.assertEqual(len(hadith_text), 796)        
        

if __name__ == '__main__':
    unittest.main()
