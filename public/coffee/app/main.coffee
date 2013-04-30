define ["app", "router", "backbone", "facebook", "../views/base/base"], (App, Router, Backbone, FB, BaseView) ->
  init = ->
    FB.init
      appId: App.Config.FB_APP_ID,
      status: true, # check login status
      cookie: true, # enable cookies to allow the server to access the session
      xfbml: true # parse XFBML

    # Backbone boilerplate auto-linking w router
    $(document).on 'click', 'a:not([data-bypass])', (event) ->
      href = $(this).attr 'href'
      protocol = this.protocol + '//'

      if href and href.slice 0, protocol.length isnt protocol and href.indexOf 'javascript:' isnt 0
        do event.preventDefault
        Backbone.history.navigate href, true

    AppView = new BaseView()
    App.State.BaseView = AppView

    Router.init()

  init: init