import unittest

import sys
sys.path.append('../GradientDescent/')

import GradientDescent as gd

class TestDistance(unittest.TestCase):
    def test(self):

        v1 = [1,5,8]
        v2 = [3,6,7]

        self.assertEqual(round(gd.distance(v1,v2), 5), 2.44949)

if __name__ == '__main__':
    unittest.main()