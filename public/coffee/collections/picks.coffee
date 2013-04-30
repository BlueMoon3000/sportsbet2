define ["app", "models", "jquery", "underscore", "backbone", "../collections/base"], (App, Models, $, _, Backbone, BaseCollection) ->
  class Picks extends BaseCollection
    model: Models.Pick
    url: 'api/v1/pick/'
    urlRoot: App.Config.ROOT_URL + this.url
  App.Collections.Picks = Picks