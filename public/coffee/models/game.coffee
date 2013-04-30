define ["app", "jquery", "underscore", "backbone", "../models/base"], (App, $, _, Backbone, BaseModel) ->
  App.Models.Game = class Game extends BaseModel
    modelClass = this.constructor.name.toLowerCase()
    urlRoot: App.Config.ROOT_URL + 'api/v1/game/'

    defaults: -> _.extend this.constructor.__super__.defaults(this)