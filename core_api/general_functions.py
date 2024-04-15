import uuid
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def generate_uuid():
    uid = uuid.uuid4().hex[-8:]
    return uid

def  validate_emailAdd(value):
    try:
        validate_email(value)
    except ValidationError as e:
        return False
    else:
        return True