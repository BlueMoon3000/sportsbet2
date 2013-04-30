from core.models import *
from core.base import JSONEncoder
from django.conf.urls.defaults import *
from django.http import HttpResponse
from django.utils import simplejson
from django.views.generic import View
from django.db.models.loading import get_model
#import settings


class JSONResponseMixin(object):
    def render_to_response(self, obj=None, version=None, **response_kwargs):
        return self.render(obj, error=False, version=version, **response_kwargs)

    def render_to_error(self, code, obj=None, version=None, **response_kwargs):
        ERROR_CODES = {
            1: 'No Matching Objects'
        }


        response_kwargs['status'] = 200
        obj = {
            'error': True,
            'code': code,
            'message': ERROR_CODES[code]
        }
        return self.render(obj, error=True, version=version, **response_kwargs)

    def render(self, obj, error, version, **response_kwargs):
        response_kwargs['content_type'] = 'application/json'
        resp = {}
        if error:
            resp['error'] = obj
        else:
            resp['response'] = obj
        resp['version'] = version

        return HttpResponse(simplejson.dumps(resp, separators=(',', ':'), indent=None, cls=JSONEncoder), **response_kwargs)


class APIBase(View, JSONResponseMixin):
    '''
    This class implements the default behavior for HTTP request methods in a RESTful manner.
    The method handlers can be subclassed in order to prevent or allow different behaviors for
    different model types.
    '''
    ERR_INVALID_REQUEST = 400
    ERR_NO_PERMISSION = 401
    ERR_FORBIDDEN = 403
    ERR_NOT_FOUND = 404
    ERR_UNPROCESSABLE = 422
    ERR_SERVER_ERROR = 500

    # Get = list all
    # Put = update one
    # Post = create one
    # Delete = remove one

    # FIXME: Going to need to go through here and make sure this is like even vaguely secure...
    # I.E What write/delete permissions can the client have?

    def get_model(self, model):
        return get_model('core', model)

    def get_obj(self, data):
        data = simplejson.loads(data)
        del(data['model'])
        return data

    def get(self, request, version, model, id=None, *args, **kwargs):
        model = self.get_model(model)
        if id:
            # FIXME: This is a hack but for now this is how we handle get requests by non-ID params...
            query = {}
            if id == 'findOne':
                query.update(request.REQUEST)
            else:
                query.update({'id': id})
            try:
                objs = model.objects.get(**query)
            except model.DoesNotExist:
                return self.render_to_error(1)
        else:
            objs = model.objects.filter(**request.REQUEST)
        return self.render_to_response(objs)

    def post(self, request, version, model, *args, **kwargs):
        data = self.get_obj(request.body)
        print(data)
        model = self.get_model(model)
        obj = model.objects.create(**data)
        return self.render_to_response(obj)

    def put(self, request, model, version, id, *args, **kwargs):
        model = self.get_model(model)
        obj = model.objects.get(pk=id)
        # FIXME: Update code here... too lazy to figure out this part for now.
        return self.render_to_response(obj)

    def delete(self, request, *args, **kwargs):
        model = self.get_model(model)
        model.objects.get(pk=id).delete()
        return self.render_to_response({'success': True})
