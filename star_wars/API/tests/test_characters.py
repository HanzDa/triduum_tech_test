from django.test import TestCase

from API.models import Character, Planet, Film


class CharacterTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.character1 = Character.objects.create(**{
                "name": "Clark",
                "gender": "female",
                "age": 6,
                "skin_color": "silver",
                "eye_color": "silver",
                "height": 75,
                "mass": 26
            })
        cls.character2 = Character.objects.create(**{
                "name": "Cali",
                "gender": "female",
                "age": 6,
                "skin_color": "teal",
                "eye_color": "green",
                "height": 73,
                "mass": 140
            })
        cls.character3 = Character.objects.create(**{
                "name": "Forest",
                "gender": "male",
                "age": 9,
                "skin_color": "red",
                "eye_color": "olive",
                "height": 154,
                "mass": 39
        })

        cls.planet = Planet.objects.create(**{
            "name": "Morocco",
            "diameter": "2",
            "gravity": 105,
            "population": 21,
            "climate": "orange"
        })
        
        cls.film = Film.objects.create(**{
            "title": "Mayer - Paucek",
            "opening_crawl": "Nam vero vitae. Nam rerum sint aliquid adipisci aliquam doloribus sequi reprehenderit. Doloremque alias provident maxime necessitatibus.",
            "directors": [
                "Dr. Matthew Satterfield",
                "Valerie McDermott"
            ],
            "producers": [
                "Nancy Toy",
                "Dexter Langosh"
            ],
            "release_date": "1970-02-22"
        })
        
    def test_creation_resident(self):
        response = self.client.get(
            '/api/v1/character/1/'
            )
        self.assertEqual(response.status_code, 401) # unauthorized user
        # TODO: create authentication test
        # TODO: add more test
