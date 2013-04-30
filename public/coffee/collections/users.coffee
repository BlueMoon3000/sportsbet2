define ["app", "models", "jquery", "underscore", "backbone", "../collections/base"], (App, Models, $, _, Backbone, BaseCollection) ->
  class Users extends BaseCollection
    model: Models.User
    url: 'api/v1/appuser/'
    urlRoot: App.Config.ROOT_URL + this.url
  App.Collections.Users = new Users