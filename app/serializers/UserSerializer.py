
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from app.models import User
from django.contrib.auth.models import Group

class UserSerializer(ModelSerializer):
    groups = SerializerMethodField()

    class Meta:
        model = User
        #fields = '__all__'
        fields = ('id', 'first_name', 'last_name', 'email', 'groups')

    def get_groups(self, user):
        groups = user.groups.all()
        groups_array = []
        for group in groups:
            data = {
                'id': group.pk,
                'name': group.name
            }
            groups_array.append(data)
        return  groups_array