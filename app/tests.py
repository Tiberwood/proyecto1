from django.test import TestCase
from django.contrib.auth.models import User, Group
from .models import Role

# Create your tests here.

class RoleTest(TestCase):

    def setUp(self):
        Role.objects.create(name='Role 1')
        Role.objects.create(name='Role 2')
    
    def test_pk(self):
        rol1 = Role.objects.get(name='Role 1') # 1 valor                        0                       1   2
        rol2 = Role.objects.filter(name='Role 2') # arreglo de objectos [ { 'id': 1, 'name': 'value' }, {}, {} ]
        self.assertEqual(rol1.name, 'Role 1')
        self.assertEqual(rol2[0].name, 'Role 2')

    def test_count(self):
        roles = Role.objects.all()
        self.assertEqual(roles.count(), 2)

class UserTest(TestCase):

    def setUp(self):
        group = Group.objects.create(pk=1, name='Grupo 1')
        group.permissions.add(1, 2, 3, 4, 7, 10)
        user = User.objects.create(pk=1, username='test 1')
        group.user_set.add(user)
        User.objects.create(pk=2, username='test 2', is_active=False)
    
    def test_permissions(self):
        users = User.objects.filter(groups=1)
        self.assertEqual(users.count(), 1)

    def test_cancel_user(self):
        user = User.objects.filter(is_active=False)
        self.assertEqual(user.count(), 1)