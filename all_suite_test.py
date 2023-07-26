import unittest

from unittest.loader import makeSuite

from test_cases.add_player import TestAdding
from test_cases.wrong_password import TestLoginWP
from test_cases.Wrong_login import TestLoginWL
from test_cases.login_to_system_correct import TestLoginCorrect
from test_cases.Leangue_change import TestLeangue




def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestAdding))
   test_suite.addTest(makeSuite(TestLoginWP))
   test_suite.addTest(makeSuite(TestLoginWL))
   test_suite.addTest(makeSuite(TestLoginCorrect))
   test_suite.addTest(makeSuite(TestLeangue))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())