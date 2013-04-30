define ["app", "models", "collections", "jquery", "underscore", "backbone", "facebook", "text!/templates/index/index.html"], (App, Models, Collections, $, _, Backbone, FB, indexTemplate) ->
  class indexView extends Backbone.View
    events:
      "click a.facebook-login": "login"

    render: ->
      $(@el).append _.template(indexTemplate)

    remove: ->
      $(@el).empty()

    login: ->
      FB.login (response) ->
        if response.authResponse
          FB.api '/me', (response) ->
            user = new Models.User
            user.fb_sync response
            user.getOrCreate fb_user_id: response.id, 
              success: (model, response) -> 
                console.log 'Good to see you ' + user.get('first_name') + '.'
                App.Collections.Users.add(user)
                App.State.User = user
                App.Routers.Router.navigate('home', true)
              error: (model, response) -> console.log response
        else
          console.log('User cancelled.')
      , scope: 'email'