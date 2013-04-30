define ["app", "backbone"], (App, Backbone) ->
  App.Collections.BaseCollection = class BaseCollection extends Backbone.Collection
    parse: (response) ->
        return response.response