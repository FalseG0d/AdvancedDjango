from django.test import TestCase
from Columbus.models import Name

class BasicTest(TestCase):
    def test_entry(self):
        name=Name()
        name.name="Test Name"
        name.save()

        record=Name.objects.get(pk=name.id)
        self.assertEqual(record,name)