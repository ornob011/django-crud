from django.db import models

class Parent(models.Model):
    """
    Model representing a parent user with full address details.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.street}, {self.city}, {self.state}, {self.zip_code}"

class Child(models.Model):
    """
    Model representing a child user linked to a Parent. Child does not have an address.
    """
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name="children")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Child of {self.parent.first_name} {self.parent.last_name})"

