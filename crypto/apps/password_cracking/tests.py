import hashlib

from django.test import TestCase

from .services import CrackingService


class TestPasswordCrackingService(TestCase):

    service = CrackingService()

    def test_generate_combinations(self):
        self.assertListEqual(['aa', 'ab', 'ba', 'bb'], list(self.service.generate_combinations('ab', 2)))

    def test_brute_force(self):
        # we arent using longer words because testing would take longer
        test_words = ['sef', 'ant', 'ng8']

        def encrypt(value: str) -> str:
            return hashlib.sha1(value.encode('utf-8')).hexdigest()

        for word in test_words:
            self.assertEqual(word, self.service.brute_force(encrypt(word), len(word), encrypt).keyword)

    def test_dictionary(self):
        dictionary = [b'1', b'2', b'three', b'4', b'8', b'10', b'twenty']

        def encrypt(value: str) -> str:
            return hashlib.sha1(value.encode('utf-8')).hexdigest()

        test_words = ['4', 'three']
        for word in test_words:
            self.assertEqual(word, self.service.crack(encrypt(word), dictionary, encrypt).keyword)

        test_words = ['5', 'six']
        for word in test_words:
            self.assertIsNone(self.service.crack(encrypt(word), dictionary, encrypt).keyword)
