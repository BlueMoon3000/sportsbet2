(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  define(["app", "models", "jquery", "underscore", "backbone", "../collections/base"], function(App, Models, $, _, Backbone, BaseCollection) {
    var Games, _ref;

    Games = (function(_super) {
      __extends(Games, _super);

      function Games() {
        _ref = Games.__super__.constructor.apply(this, arguments);
        return _ref;
      }

      Games.prototype.model = Models.Game;

      Games.prototype.url = 'api/v1/game/';

      Games.prototype.urlRoot = App.Config.ROOT_URL + Games.url;

      return Games;

    })(BaseCollection);
    return App.Collections.Games = new Games;
  });

}).call(this);
