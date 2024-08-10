from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'rolled', 'address']

        def __init__(self,request, *args, **kwargs):
            super(StudentSerializer, self).__init__(*args, **kwargs)
            if request.method in ['POST', 'PUT']:
                self.fields['name'].required = True
                self.fields['rolled'].required = True
                self.fields['address'].required = True
            elif request.method == 'GET':
                self.fields['name'].read_only = True
                self.fields['rolled'].read_only = True
                self.fields['address'].read_only = True