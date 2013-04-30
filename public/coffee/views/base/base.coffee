define ["app", "jquery", "underscore", "backbone", "facebook", "text!/templates/base/base.html"], (App, $, _, Backbone, FB, baseTemplate) ->
  class baseView extends Backbone.View
    el: "body"
    elChild: ".span12"

    initialize: ->
        this.render()

    render: ->
      $(@el).append _.template(baseTemplate)