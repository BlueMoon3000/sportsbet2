define ["app", "models", "jquery", "underscore", "backbone", "text!/templates/home/game.html"], (App, Models, $, _, Backbone, gameTemplate) ->
  class gameView extends Backbone.View
    events:
      "click a.team-select": "submitPick"

    initialize: () ->
      this.options.picks.bind('add', this.render, this)

    submitPick: (event) ->
      event.preventDefault()
      if $(event.currentTarget).hasClass('away')
        team_id = this.model.get('away').id
      else
        team_id = this.model.get('home').id

      pick = new Models.Pick
        player_id: App.State.User.id
        match_id: this.options.match.id
        team_id: team_id
        game_id: this.model.id
      console.log pick
      pick.save()
      this.options.picks.add(pick)

    render: ->
      $(@el).empty()
      picks = null
      if this.options.picks.length != 0
        picks = this.options.picks.toJSON()
      $(@el).append _.template gameTemplate, 
        _: _
        game: this.model.toJSON()
        picks: _.where picks, game_id:this.model.id
      
  return gameView