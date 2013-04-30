define ["app", "../models/base", "jquery", "underscore", "backbone"], (App, BaseModel, $, _, Backbone) ->
  App.Models.User = class AppUser extends BaseModel
    modelClass = this.constructor.name.toLowerCase()
    urlRoot: App.Config.ROOT_URL + 'api/v1/appuser/'

    defaults: -> _.extend this.constructor.__super__.defaults(this),
      id: 'findOne' # BIGGEST HACK IN THE WORLD
      email: null
      fb_user_id: null
      fb_access_token: null

    is_authenticated: ->
      fb_user_id and fb_access_token

    fb_sync: (data) ->
      this.set 
        fb_user_id: data.id
        full_name: data.name
        first_name: data.first_name
        last_name: data.last_name
        email: data.email