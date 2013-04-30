from django.db.models.query import QuerySet
from django.db.models import Model
from django.utils import simplejson
import calendar
import datetime


class JSONEncoder(simplejson.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, QuerySet):
            return [item.serializable_dict(version=self._api_version) for item in obj]
        elif isinstance(obj, Model):
            return obj.serializable_dict(version=self._api_version)
        elif isinstance(obj, datetime.datetime):
            return calendar.timegm(obj.timetuple())
        else:
            return simplejson.JSONEncoder.default(self, obj)

    def encode(self, obj):
        self._api_version = obj['version']
        del(obj['version'])
        return super(JSONEncoder, self).encode(obj)
