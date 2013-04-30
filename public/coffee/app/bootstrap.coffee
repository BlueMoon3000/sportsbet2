require.config
  paths:
    jquery: '//ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min'
    underscore: '../lib/underscore/underscore.min'
    backbone: '../lib/backbone/backbone.min'
    backboneInheritance: '../lib/backbone/backbone-inheritance'
    facebook: '//connect.facebook.net/en_US/all'
    text: '../lib/require/text'

  shim:
    underscore:
      exports: "_"
    facebook:
      exports: "FB"

    backbone:
      deps: ["underscore", "jquery"]
      exports: "Backbone"

require ["main"], (Main) ->
  Main.init()