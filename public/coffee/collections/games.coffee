define ["app", "models", "jquery", "underscore", "backbone", "../collections/base"], (App, Models, $, _, Backbone, BaseCollection) ->
  class Games extends BaseCollection
    model: Models.Game
    url: 'api/v1/game/'
    urlRoot: App.Config.ROOT_URL + this.url
  App.Collections.Games = new Games