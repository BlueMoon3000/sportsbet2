define ["app", "models", "jquery", "underscore", "backbone", "../home/game"], (App, Models, $, _, Backbone, GameView) ->
  class gamesView extends Backbone.View
    initialize: () ->
      this.listenTo(App.Collections.Games, 'add', this.addOne)

      this._childViews = []
      self = this
      this.picks = new App.Collections.Picks
      this.picks.fetch
        data: match_id: this.options.match.id
        processData: true
        success: (collection, response) ->
          self.collection.fetch
            success: (collection, response) -> console.log collection, response
            error: () -> console.log 'hi'

      setInterval () ->
        self.updatePicks()
      , 5000

      this.picks.bind('add', this.update, this)

    updatePicks: () ->
      this.picks.fetch
        data: match_id: this.options.match.id
        processData: true
        update: true

    addOne: (game) ->
      gameView = new GameView 
        model:game
        picks: this.picks
        match: this.options.match
      gameView.render()
      this._childViews.push(gameView)
      this.$el.append(gameView.el)

    update: ->
      console.log this.picks
      
      
  return gamesView