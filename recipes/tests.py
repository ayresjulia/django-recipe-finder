from django.test import TestCase
from http import HTTPStatus
from .forms import RecipeForm

# testing email error, home '/' route, form submission and redirection to 'thankyou/<int:id>'


class RecipeFormTestCase(TestCase):
    def test_home_form(self):
        form = RecipeForm(data={'first_name': "John", 'last_name': "Smith",
                                'email': 'john', 'child_first_name': 'Bob', 'child_last_name': 'Smith'})

        self.assertEqual(form.errors["email"], [
            "Enter a valid email address."])

    def test_get_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(
            response, "Tiny Organics recipe finder", html=True)

    def test_post_success(self):
        response = self.client.post(
            "/", data={'first_name': "John", 'last_name': "Smith", 'email': 'john@js.com', 'child_first_name': 'Bob', 'child_last_name': 'Smith'}
        )

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], "thankyou/1/")
