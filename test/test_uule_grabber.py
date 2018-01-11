""" unit tests for uule grabber """
import unittest
import uule_grabber


class TestUuleGrabber(unittest.TestCase):
    """ uule_grabber tests """

    def test_uule_secret(self):
        """ Checks UULE secret code algorithm  """
        control_list = [(4, "E"), (25, "Z"), (26, "a"),
                        (43, "r"), (51, "z"), (52, "0"),
                        (61, "9"), (62, "-"), (63, "_"),
                        (64, "A"), (76, "M"), (83, "T")]
        for value, expected in control_list:
            self.assertEqual(uule_grabber.uule_secret(value),
                             expected, "Control value: {}".format(value))

    def test_uule(self):
        """ Checks UULE code algorithm """
        control_list = [("Lezigne,Pays de la Loire,France", "w+CAIQICIfTGV6aWduZSxQYXlzIGRlIGxhIExvaXJlLEZyYW5jZQ"),
                        ("Reze,Pays de la Loire,France",
                         "w+CAIQICIcUmV6ZSxQYXlzIGRlIGxhIExvaXJlLEZyYW5jZQ"),
                        ("Chicago,Illinois,United States",
                         "w+CAIQICIeQ2hpY2FnbyxJbGxpbm9pcyxVbml0ZWQgU3RhdGVz"),
                        ("Washington,District of Columbia,United States",
                         "w+CAIQICItV2FzaGluZ3RvbixEaXN0cmljdCBvZiBDb2x1bWJpYSxVbml0ZWQgU3RhdGVz"),
                        ("Jacksonville Beach,Florida,United States", "w+CAIQICIoSmFja3NvbnZpbGxlIEJlYWNoLEZsb3JpZGEsVW5pdGVkIFN0YXRlcw")]
        for value, expected in control_list:
            self.assertEqual(uule_grabber.uule(value),
                             expected, "Control value: {}".format(value))


if __name__ == '__main__':
    unittest.main()
