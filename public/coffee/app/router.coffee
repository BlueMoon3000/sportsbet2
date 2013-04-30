define ["app", "jquery", "underscore", "backbone", "../views/index/index", "../views/home/home"], (App, $, _, Backbone, indexView, homeView) ->
  class AppRouter extends Backbone.Router
    routes:
      "": "index"
      "home": "home"

    navigate: ->
      $(App.State.currentView.el).empty()
      App.State.currentView.unbind()
      App.State.currentView = null;
      super

    index: ->
      index = new indexView el: App.State.BaseView.elChild
      this.render index

    home: ->
      home = new homeView el: App.State.BaseView.elChild
      this.render home

    render: (view) ->
      App.State.currentView = view
      App.State.currentView.render()

  init = ->
    App.Routers.Router = new AppRouter
    Backbone.history.start({pushState: true})


  init: init