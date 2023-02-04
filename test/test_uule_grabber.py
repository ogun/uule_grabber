""" unit tests for uule grabber """
import unittest
import uule_grabber


class TestUuleGrabber(unittest.TestCase):
    """uule_grabber tests"""

    def test_uule(self):
        """Checks UULE code algorithm"""
        control_list = [
            (
                "Lezigne,Pays de la Loire,France",
                "w+CAIQICIfTGV6aWduZSxQYXlzIGRlIGxhIExvaXJlLEZyYW5jZQ",
            ),
            (
                "Reze,Pays de la Loire,France",
                "w+CAIQICIcUmV6ZSxQYXlzIGRlIGxhIExvaXJlLEZyYW5jZQ",
            ),
            (
                "Chicago,Illinois,United States",
                "w+CAIQICIeQ2hpY2FnbyxJbGxpbm9pcyxVbml0ZWQgU3RhdGVz",
            ),
            (
                "Washington,District of Columbia,United States",
                "w+CAIQICItV2FzaGluZ3RvbixEaXN0cmljdCBvZiBDb2x1bWJpYSxVbml0ZWQgU3RhdGVz",
            ),
            (
                "Jacksonville Beach,Florida,United States",
                "w+CAIQICIoSmFja3NvbnZpbGxlIEJlYWNoLEZsb3JpZGEsVW5pdGVkIFN0YXRlcw",
            ),
            (
                "BURGERHEIM, Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße 8, 84130 Dingolfing, Germany",
                "w+CAIQICIdQlVSR0VSSEVJTSwgQmlzY2jDtmZsaWNoLUdlaXN0bGljaGVyLVJhdC1Kb3NlZi1aaW5uYmF1ZXItU3RyYcOfZSA4LCA4NDEzMCBEaW5nb2xmaW5nLCBHZXJtYW55",
            ),
        ]
        for value, expected in control_list:
            with self.subTest():
                self.assertEqual(
                    uule_grabber.uule(value),
                    expected,
                    "Control value: {}".format(value),
                )


if __name__ == "__main__":
    unittest.main()
