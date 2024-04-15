from rest_framework import serializers
from ..models.consumer_model import *

class ConsumerProfileSerializer(serializers.ModelSerializer):

    consumer_name = serializers.Charfield(source='name')

    class Meta:

        model = ConsumerModel
        fields = (
            'profile_id',
            'name',
            'birthdate',
            'mobile_number',
            'gender',
            'profile_image'
                  )
        
        def to_representation(self,instance):
            ret = super().to_representation(instance)
            ret['gender'] = str(instance.gender).title()
            return ret
        
    
        



