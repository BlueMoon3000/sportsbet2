from django.db import models
from django.utils.encoding import smart_unicode

import settings

class SerializeMixin:
    def serializable_dict(self, version=None, **kwargs):
        rv = {'pk': self.pk, 'model': smart_unicode(self._meta)}
        # skip = ['id']
        skip = []
        options = self.serialize_options(version)

        if settings.SERIALIZE_FLATTEN_MODELS:
            field_obj = rv
        else:
            rv['fields'] = {}
            field_obj = rv['fields']

        for field in self._meta.fields:
            if 'excludes' in options and field.name in options['excludes'] or field.name in skip:
                continue
            elif 'relations' in options and field.name in options['relations']:
                if getattr(self, field.name):
                    field_obj[field.name] = getattr(self, field.name).serializable_dict(version)
                else:
                    field_obj[field.name] = getattr(self, field.name)
                if settings.SERIALIZE_INCLUDE_ID_REF:
                    field_obj['%s_id' % field.name] = getattr(self, '%s_id' % field.name)
            else:
                if isinstance(field, models.ForeignKey):
                    field_obj[field.name] = getattr(self, '%s_id' % field.name)
                    if settings.SERIALIZE_INCLUDE_ID_REF:
                        field_obj['%s_id' % field.name] = getattr(self, '%s_id' % field.name)
                else:
                    field_obj[field.name] = getattr(self, field.name, None)

        if 'extras' in options:
            for field in options['extras']:
                res = getattr(self, field)(version)
                if field.startswith('ser_'):
                    field = field.replace('ser_', '', 1)
                field_obj[field] = res

        if 'flatten' in options:
            for field in options['flatten']:
                for k, v in getattr(self, field)(version).iteritems():
                    field_obj[k] = v

        # Allow for some serialize options to only be triggered when required.
        if 'extensions' in kwargs:
            for field in kwargs['extensions']:
                if field in options['extensions']:
                    res = getattr(self, field)(version)
                    if field.startswith('flatten_'):
                        for k,v in res.iteritems():
                            field_obj[k] = v
                        break

                    if field.startswith('ser_'):
                        field = field.replace('ser_', '', 1)
                    field_obj[field] = res

        return rv

    def serialize_options(self, version=None):
        '''
        Passes serialization options to the serializable_dict method above:
            - excludes: fields to be removed from the serializable_dict
            - extras: arbitrary extra fields to add based on a function response. 
                *if 'ser_' prefix is included that will be stripped from the key in the serializable_dict.
            - flatten: flattens a dictionary into the serializable_dict
            - relations: fields to be populated from a foreign key reference
            - extensions: fields to be optionally serialized depending on context

        Note that there is no error handling in the case that you don't follow the format specified above. So shit will break. Horribly.
        '''
        return {}
