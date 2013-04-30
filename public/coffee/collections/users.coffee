define ["app", "models", "jquery", "underscore", "backbone", "../collections/base"], (App, Models, $, _, Backbone, BaseCollection) ->
  class Users extends BaseCollection
    model: Models.User
    url: '/api/v1/appuser/'
    urlRoot: 'http://local.host:8000' + this.url
  App.Collections.Users = new Users