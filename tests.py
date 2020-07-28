"""Tests for Balloonicorn's Flask app."""

# you must import unittest to test Flask
import unittest
# you must import your main py file
import server


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Code to run before every test."""

        print('FIXED BELOW')
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_homepage(self):
        """Can we reach the homepage?"""

        print('FIXED BELOW - provide result then self assertion type b phrase in page, get result of data')
        result = self.client.get('/')
        self.assertIn(b'having a party', result.data)

    def test_no_rsvp_yet(self):
        """Do users who haven't RSVPed see the correct view?"""

        # FIXME: Add a test to show we haven't RSVP'd yet
        print('FIXED BELOW - provide result then self assertion type b phrase in page, get result of data')
        result = self.client.get('/')
        self.assertIn(b'Please RSVP', result.data)

    def test_rsvp(self):
        """Do RSVPed users see the correct view?"""

        rsvp_info = {'name': 'Jane', 'email': 'jane@jane.com'}

        result = self.client.post('/rsvp', data=rsvp_info,
                                  follow_redirects=True)

        # FIXME: check that once we log in we see party details--but not the form!
        print('FIXED BELOW - provide for variable, dictionary of data and result self clent post to route data variable and True follow redirects then self assertion type b phrase in page, get result of data')
        rsvp_info = {'name': 'Jane', 'email': 'jane@jane.com'}

        result = self.client.post('/rsvp', data=rsvp_info,
                                  follow_redirects=True)
# The following lines were required

        # Generic pattern: self.assertSomething(b'What to say', result.data)
        
        # longer list in lecture of magic assertions

        # assertEqual(a, b) | a == b

        # assertNotEqual(a, b) | a != b

        # assertTrue(x) | bool(x) is True

        # assertFalse(x) | bool(x) is False

        # assertIs(a, b) | a is b

        # assertIsNot(a, b) | a is not b

        # assertIsNone(x) | x is None

        # assertIsNotNone(x) | x is not None

        # assertIn(a, b) | a in b

        # assertNotIn(a, b) | a not in b

        # assertIsInstance(a, b) | isinstance(a, b)

        # assertNotIsInstance(a, b)  | not isinstance(a, b)

        self.assertIn(b'Yay!', result.data)
        self.assertIn(b'Party Details', result.data)
        self.assertNotIn(b'Please RSVP', result.data)

    def test_rsvp_mel(self):
        """Can we keep Mel out?"""

        # FIXME: write a test that mel can't invite himself
        # write more tests with the name different and the e-mail different and casing or use lower

        pass
        print('FIXED BELOW')
        rsvp_info = {'name': 'Mel', 'email': 'mel@ubermelon.com'}

        result = self.client.post('/rsvp', data=rsvp_info,
                                  follow_redirects=True)

        self.assertNotIn(b'Yay!', result.data)
        self.assertNotIn(b'Party Details', result.data)
        self.assertIn(b'Please RSVP', result.data)


if __name__ == '__main__':
   # to call test for Flask you must have the unittest.main() line below
    unittest.main()
