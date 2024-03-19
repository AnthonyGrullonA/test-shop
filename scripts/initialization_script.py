# initialization_script.py

from django.contrib.auth.models import Group
from django.db import transaction

def create_roles():
    roles = ["Access", "Admin", "Client"]
    with transaction.atomic():
        for role_name in roles:
            group, created = Group.objects.get_or_create(name=role_name)
            if created:
                print(f"Se creó el rol: {role_name}")
            else:
                print(f"El rol {role_name} ya existe en la base de datos.")

def run():
    create_roles()

if __name__ == '__main__':
    run()
