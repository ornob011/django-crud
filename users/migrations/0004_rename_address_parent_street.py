# Generated by Django 4.2.7 on 2023-12-01 08:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_child_parent_remove_user_parent_id_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="parent",
            old_name="address",
            new_name="street",
        ),
    ]
