define ["app", "jquery", "underscore", "backbone", "../models/base"], (App, $, _, Backbone, BaseModel) ->
  App.Models.Match = class Match extends BaseModel
    modelClass = this.constructor.name.toLowerCase()
    urlRoot: 'http://local.host:8000/api/v1/match/'

    defaults: -> _.extend this.constructor.__super__.defaults(this)