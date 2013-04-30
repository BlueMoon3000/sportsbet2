define ["app", "models", "jquery", "underscore", "backbone", "../home/games", "text!/templates/home/match.html"], (App, Models, $, _, Backbone, GamesView, matchTemplate) ->
  class matchView extends Backbone.View
    render: ->
      $(@el).empty() # Probably better way to remove the old view...
      match = null
      if this.model
        match = this.model.toJSON()

      $(@el).append _.template matchTemplate, 
        match: match
        error: this.options.error

      if this.model
        gamesView = new GamesView
          el: this.$('.games-container')
          match: this.model
          collection: App.Collections.Games

  return matchView