import unittest
from unittest.mock import patch

from patterns.creational.abstract_factory import PetShop, Dog


class TestPetShop(unittest.TestCase):
    def test_dog_pet_shop_shall_show_dog_instance(self):
        dog_pet_shop = PetShop(Dog)
        with patch.object(Dog, 'speak') as mock_Dog_speak:
            dog_pet_shop.show_pet()
            self.assertEqual(mock_Dog_speak.call_count, 1)
