# Django-serialize settings
# Default values will only be used if no other values are specified

from django.conf import settings

SERIALIZE_FLATTEN_MODELS = getattr(settings, 'SERIALIZE_FLATTEN_MODELS', False)
SERIALIZE_INCLUDE_ID_REF = getattr(settings, 'SERIALIZE_INCLUDE_ID_REF', False)
