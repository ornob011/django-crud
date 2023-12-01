from django.test import TestCase, Client
from django.urls import reverse
from .models import Parent, Child

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.parent = Parent.objects.create(
            first_name='John',
            last_name='Doe',
            address='123 Main St',
            city='Anytown',
            state='Anystate',
            zip_code='12345'
        )
        self.child = Child.objects.create(
            first_name='Jane',
            last_name='Doe',
            parent=self.parent
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')
        self.assertTemplateUsed(response, 'home.html')

    def test_list_parents_view(self):
        response = self.client.get(reverse('list_parents'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')
        self.assertTemplateUsed(response, 'list_parents.html')

    def test_list_children_view(self):
        response = self.client.get(reverse('list_children'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jane Doe')
        self.assertTemplateUsed(response, 'list_children.html')

    def test_create_parent_view_get(self):
        response = self.client.get(reverse('create_parent'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_update_parent.html')

    def test_create_parent_view_post(self):
            response = self.client.post(reverse('create_parent'), {
                'first_name': 'Alice',
                'last_name': 'Smith',
                'address': '456 Elm Street',
                'city': 'Springfield',
                'state': 'SP',
                'zip_code': '67890'
            })
            self.assertEqual(response.status_code, 302)  # Redirects after creation
            self.assertEqual(Parent.objects.count(), 2)

    def test_update_parent_view_post(self):
        response = self.client.post(reverse('update_parent', args=[self.parent.id]), {
            'first_name': 'John',
            'last_name': 'Doe Updated',
            'address': '123 Main St',
            'city': 'Anytown',
            'state': 'Anystate',
            'zip_code': '12345'
        })
        self.assertEqual(response.status_code, 302)  # Redirects after update
        self.parent.refresh_from_db()
        self.assertEqual(self.parent.last_name, 'Doe Updated')

    def test_delete_parent_view(self):
        response = self.client.post(reverse('delete_parent', args=[self.parent.id]))
        self.assertEqual(response.status_code, 302)  # Redirects after deletion
        self.assertEqual(Parent.objects.count(), 0)

    def test_create_child_view_post(self):
            response = self.client.post(reverse('create_child'), {
                'first_name': 'Bob',
                'last_name': 'Doe',
                'parent': self.parent.id
            })
            self.assertEqual(response.status_code, 302)  # Redirects after creation
            self.assertEqual(Child.objects.count(), 2)

    def test_update_child_view_post(self):
        response = self.client.post(reverse('update_child', args=[self.child.id]), {
            'first_name': 'Jane',
            'last_name': 'Doe Updated',
            'parent': self.parent.id
        })
        self.assertEqual(response.status_code, 302)  # Redirects after update
        self.child.refresh_from_db()
        self.assertEqual(self.child.last_name, 'Doe Updated')

    def test_delete_child_view(self):
        response = self.client.post(reverse('delete_child', args=[self.child.id]))
        self.assertEqual(response.status_code, 302)  # Redirects after deletion
        self.assertEqual(Child.objects.count(), 0)