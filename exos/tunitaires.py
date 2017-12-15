#! /usr/bin/env python3

import unittest
import vieux

class WidgetTestCase(unittest.TestCase):

    def test_vieux_raise_type(self):
        with self.assertRaises(vieux.AgeMauvaisType):
            vieux.vieux(0.0)
        with self.assertRaises(vieux.AgeMauvaisType):
            vieux.vieux(1.0)
        with self.assertRaises(vieux.AgeMauvaisType):
            vieux.vieux(-1.0)
        with self.assertRaises(vieux.AgeMauvaisType):
            vieux.vieux('1.0')
        with self.assertRaises(vieux.AgeMauvaisType):
            vieux.vieux(1j)
        with self.assertRaises(vieux.AgeMauvaisType):
            vieux.vieux(None)

    def test_vieux_raise_value(self):
        with self.assertRaises(vieux.AgeNegatif):
            vieux.vieux(-12)
        with self.assertRaises(vieux.AgeNegatif):
            vieux.vieux(-1)
        with self.assertRaises(vieux.AgeInvalide):
            vieux.vieux(0)

    def test_vieux(self):
        self.assertFalse(vieux.vieux(1))
        self.assertFalse(vieux.vieux(vieux._AGE_LIMITE - 1))
        self.assertTrue(vieux.vieux(vieux._AGE_LIMITE))
        self.assertTrue(vieux.vieux(vieux._AGE_LIMITE + 1))
        self.assertTrue(vieux.vieux(999))

if __name__ == '__main__':
    unittest.main()
