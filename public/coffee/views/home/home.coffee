define ["app", "models", "jquery", "underscore", "backbone", "../home/match","text!/templates/home/home.html"], (App, Models, $, _, Backbone, MatchView, homeTemplate) ->
  class homeView extends Backbone.View
    events:
      "click button.create-game": "createMatch"
      "keyup input.game-code": "retrieveMatch"
      "click input.game-code-submit": "retrieveMatch"

    retrieveMatch: (event) ->
      # Really need to update this code and stop using the findOne hack...
      if event.type != 'keyup' or event.type == 'keyup' and event.keyCode == 13
        code = this.$('.game-code').val() or null
        match = new Models.Match id: 'findOne'
        match.fetch 
          data: 
            code: code
          processData: true
          success: (model, response) ->
            error = null
            if response.error and response.error.code == 1
              error = 'No match was found with the given code, try starting a new game instead.'
              match = null
            matchView = new MatchView
              el: this.$('.match-container')
              model: match
              error: error
            matchView.render()
          error: (model, response) ->
            console.log response

    createMatch: ->
      match = new App.Models.Match
      match.set player_id:App.State.User.id
      match.save {},
        success: (model, response) ->
          matchView = new MatchView 
            el: this.$('.match-container')
            model: match
            error: null
          matchView.render()
        error: (model, response) ->
          console.log response

    render: ->
      $(@el).append _.template homeTemplate, user: App.State.User.toJSON()