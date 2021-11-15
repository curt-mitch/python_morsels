from contextlib import contextmanager, redirect_stdout, redirect_stderr
from io import StringIO
from importlib.machinery import SourceFileLoader
from importlib.util import module_from_spec, spec_from_loader
import shlex
import sys
import unittest


class CheckHelperTests(unittest.TestCase):

    """Tests for check_helper.py."""

    maxDiff = None

    def verifyFirstLine(self, argument, expected):
        output = run_program(f"check_helper.py {argument}")
        try:
            self.assertEqual(output.splitlines()[0], expected)
        except IndexError:
            self.fail("Output of program was empty")

    def verifySecondLine(self, argument, expected):
        output = run_program(f"check_helper.py {argument}")
        try:
            try:
                self.assertEqual(output.splitlines()[1], expected)
            except AssertionError:
                if "-" not in expected:
                    raise
                expected = expected.replace("-", " ")
                self.assertEqual(output.splitlines()[1], expected)
        except IndexError:
            self.fail(f"Output has fewer than 2 lines:\n{output}")

    def assertThirdLine(self, output, expected):
        try:
            self.assertEqual(output.splitlines()[2], expected)
        except IndexError:
            self.fail(f"Output has fewer than 3 lines:\n{output}")

    def test_no_cents(self):
        self.verifyFirstLine("345", "$345.00")

    def test_prints_with_dollar_sign(self):
        self.verifyFirstLine("345.60", "$345.60")

    def test_prints_commas(self):
        self.verifyFirstLine("20345.60", "$20,345.60")

    def test_many_commas(self):
        self.verifyFirstLine("12345678.90", "$12,345,678.90")

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_words_spelled_out(self):
        self.verifySecondLine("5", "five only")
        self.verifySecondLine("10", "ten only")
        self.verifySecondLine("11", "eleven only")
        self.verifySecondLine("12", "twelve only")
        self.verifySecondLine("13", "thirteen only")
        self.verifySecondLine("14", "fourteen only")
        self.verifySecondLine("15", "fifteen only")
        self.verifySecondLine("16", "sixteen only")
        self.verifySecondLine("17", "seventeen only")
        self.verifySecondLine("18", "eighteen only")
        self.verifySecondLine("19", "nineteen only")
        self.verifySecondLine("20", "twenty only")
        self.verifySecondLine("21", "twenty-one only")
        self.verifySecondLine("30", "thirty only")
        self.verifySecondLine("32", "thirty-two only")
        self.verifySecondLine("40", "forty only")
        self.verifySecondLine("49", "forty-nine only")
        self.verifySecondLine("50", "fifty only")
        self.verifySecondLine("57", "fifty-seven only")
        self.verifySecondLine("63", "sixty-three only")
        self.verifySecondLine("74", "seventy-four only")
        self.verifySecondLine("85", "eighty-five only")
        self.verifySecondLine("96", "ninety-six only")
        self.verifySecondLine("88", "eighty-eight only")
        self.verifySecondLine("88.55", "eighty-eight and 55/100")
        self.verifySecondLine("0.02", "zero and 2/100")

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_hundred_and_thousand_words(self):
        self.verifySecondLine("305", "three hundred five only")
        self.verifySecondLine("810", "eight hundred ten only")
        self.verifySecondLine("911", "nine hundred eleven only")
        self.verifySecondLine("112", "one hundred twelve only")
        self.verifySecondLine("213", "two hundred thirteen only")
        self.verifySecondLine("414", "four hundred fourteen only")
        self.verifySecondLine("615", "six hundred fifteen only")
        self.verifySecondLine("516", "five hundred sixteen only")
        self.verifySecondLine("718", "seven hundred eighteen only")
        self.verifySecondLine("365", "three hundred sixty-five only")
        self.verifySecondLine(
            "1020",
            "one thousand twenty only",
        )
        self.verifySecondLine(
            "2421.25",
            "two thousand four hundred twenty-one and 25/100",
        )
        self.verifySecondLine("300", "three hundred only")
        self.verifySecondLine("5000", "five thousand only")

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_date(self):
        # Default format is YYYY-MM-DD
        with patch_date(2020, 1, 1):
            self.assertThirdLine(
                run_program("check_helper.py 50"),
                "2020-01-01",
            )
        with patch_date(2008, 10, 31):
            self.assertThirdLine(
                run_program("check_helper.py 50"),
                "2008-10-31",
            )
        with patch_date(2024, 2, 29):
            self.assertThirdLine(
                run_program("check_helper.py 50"),
                "2024-02-29",
            )

        # MM/DD/YY format accepted
        with patch_date(2020, 1, 1):
            self.assertThirdLine(
                run_program("check_helper.py 50 MM/DD/YY"),
                "01/01/20",
            )
        with patch_date(2008, 10, 31):
            self.assertThirdLine(
                run_program("check_helper.py 50 MM/DD/YY"),
                "10/31/08",
            )
        with patch_date(2024, 2, 29):
            self.assertThirdLine(
                run_program("check_helper.py 50 MM/DD/YY"),
                "02/29/24",
            )

        # DD.MM.YYYY format accepted
        with patch_date(2020, 1, 1):
            self.assertThirdLine(
                run_program("check_helper.py 50 DD.MM.YYYY"),
                "01.01.2020",
            )
        with patch_date(2008, 10, 31):
            self.assertThirdLine(
                run_program("check_helper.py 50 DD.MM.YYYY"),
                "31.10.2008",
            )
        with patch_date(2024, 2, 29):
            self.assertThirdLine(
                run_program("check_helper.py 50 DD.MM.YYYY"),
                "29.02.2024",
            )

        # MMM D, YYYY format accepted
        with patch_date(2020, 1, 1):
            self.assertThirdLine(
                run_program('check_helper.py 50 "MMM D, YYYY"'),
                "Jan 1, 2020",
            )
        with patch_date(2008, 10, 31):
            self.assertThirdLine(
                run_program('check_helper.py 50 "MMM D, YYYY"'),
                "Oct 31, 2008",
            )
        with patch_date(2024, 2, 29):
            self.assertThirdLine(
                run_program('check_helper.py 50 "MMM D, YYYY"'),
                "Feb 29, 2024",
            )

        # D MMMM YYYY format accepted
        with patch_date(2020, 1, 1):
            self.assertThirdLine(
                run_program('check_helper.py 50 "D MMMM YYYY"'),
                "1 January 2020",
            )
        with patch_date(2008, 10, 31):
            self.assertThirdLine(
                run_program('check_helper.py 50 "D MMMM YYYY"'),
                "31 October 2008",
            )
        with patch_date(2024, 2, 29):
            self.assertThirdLine(
                run_program('check_helper.py 50 "D MMMM YYYY"'),
                "29 February 2024",
            )


class DummyException(Exception):
    """No code will ever raise this exception."""


def run_program(arguments="", raises=DummyException):
    """
    Run program at given path with given arguments.

    If raises is specified, ensure the given exception is raised.
    """
    arguments = arguments.replace('\\', '\\\\')
    path, *args = shlex.split(arguments)
    old_args = sys.argv
    assert all(isinstance(a, str) for a in args)
    try:
        sys.argv = [path] + args
        with redirect_stdout(StringIO()) as output:
            with redirect_stderr(output):
                try:
                    if '__main__' in sys.modules:
                        del sys.modules['__main__']
                    loader = SourceFileLoader('__main__', path)
                    spec = spec_from_loader(loader.name, loader)
                    module = module_from_spec(spec)
                    sys.modules['__main__'] = module
                    loader.exec_module(module)
                except raises:
                    return output.getvalue()
                except SystemExit as e:
                    if e.args != (0,):
                        raise SystemExit(output.getvalue()) from e
                finally:
                    sys.modules['__main__'].__dict__.clear()
                    sys.modules.pop('__main__', None)  # Closes any open files
                if raises is not DummyException:
                    raise AssertionError("{} not raised".format(raises))
                return output.getvalue()
    finally:
        sys.argv = old_args


@contextmanager
def patch_date(year, month, day, hour=0, minute=0):
    """Monkey patch the current time to be the given time."""
    import datetime
    from unittest.mock import patch

    date_args = year, month, day
    time_args = hour, minute

    class FakeDate(datetime.date):
        """A datetime.date class with mocked today method."""

        @classmethod
        def today(cls):
            return cls(*date_args)

    class FakeDateTime(datetime.datetime):
        """A datetime.datetime class with mocked today, now methods."""

        @classmethod
        def today(cls):
            return cls(*date_args, *time_args)

        @classmethod
        def now(cls):
            return cls.today()

    def set_date(year, month, day, *rest):
        nonlocal date_args, time_args
        date_args = year, month, day
        time_args = rest

    FakeDate.__name__ = 'date'
    FakeDateTime.__name__ = 'datetime'
    with patch('datetime.datetime', FakeDateTime):
        with patch('datetime.date', FakeDate):
            yield set_date


if __name__ == "__main__":
    unittest.main(verbosity=2)
