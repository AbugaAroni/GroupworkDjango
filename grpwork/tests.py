from django.test import TestCase
from .models import Profile, Neighbourhood, Business_centres
from django.contrib.auth.models import User

# Create your tests here.
class Business_centresClass(TestCase):
        # Set up method
    def setUp(self):
        self.testcentre = Business_centres(centre_name="rick", contact_info="070707707", emergency_service=True)
        self.testcentre.save()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.testcentre,Business_centres))

    # Testing Save Method
    def test_save_method(self):
        self.testcentre.save_centre()
        testsaved = Business_centres.objects.all()
        self.assertTrue(len(testsaved) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.testcentre.save_centre()
        testsaved = Business_centres.objects.all()
        self.assertTrue(len(testsaved) > 0)

        self.testcentre.delete_centre()
        testdelete = Business_centres.objects.filter(centre_name="rick")
        self.assertEqual(len(testdelete), 0)

# Create your tests here.
