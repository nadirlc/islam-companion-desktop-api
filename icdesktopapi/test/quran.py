import sys,os
import unittest
sys.path.append('..')

from icdesktopapi.quran_api import Quran_Api

class TestQuran_Api(unittest.TestCase):
    """Used to test the quran api"""
 
    @classmethod
    def setUpClass(cls):
    
        # The absolute path to the database 
        cur_dir         = os.path.dirname(os.path.realpath(__file__))
        db_path         = os.path.abspath(cur_dir + "/../data/holy-quran.db")
        
        """It creates an object of type Quran_Api"""
        cls.quran_api = Quran_Api(db_path)
        
    def test_get_sura_names(self):
        """It checks if the number of suras fetched from database is 114"""

        cls       = self.__class__
        sura_list = cls.quran_api.get_sura_names()
        self.assertEqual(len(sura_list), 114)
        
    def test_get_ruku_count(self):
        """It checks if the ruku count fetched from database is 40 for sura 2
        """
        
        cls       = self.__class__        
        rukus     = cls.quran_api.get_ruku_count(2)
        self.assertEqual(rukus, 40)
        
    def test_get_ayat_range(self):
        """It checks if the ayat range for sura 1, ruku 1 is 1-7"""
        
        cls       = self.__class__
        ayat_data = cls.quran_api.get_ayat_range(1, 1)
        self.assertEqual(ayat_data['start'], 1)
        self.assertEqual(ayat_data['end'], 7)
        
    def test_get_ayat_text(self):
        """It checks if the number of ayas for sura 1, ruku 1 is 7"""
        
        cls       = self.__class__
        ayat_list = cls.quran_api.get_ayat_text(1, 1)
        self.assertEqual(len(ayat_list), 7)

if __name__ == '__main__':
    unittest.main()
