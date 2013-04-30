(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  define(["app", "jquery", "underscore", "backbone", "../models/base"], function(App, $, _, Backbone, BaseModel) {
    var Game, _ref;

    return App.Models.Game = Game = (function(_super) {
      var modelClass;

      __extends(Game, _super);

      function Game() {
        _ref = Game.__super__.constructor.apply(this, arguments);
        return _ref;
      }

      modelClass = Game.constructor.name.toLowerCase();

      Game.prototype.urlRoot = App.Config.ROOT_URL + 'api/v1/game/';

      Game.prototype.defaults = function() {
        return _.extend(this.constructor.__super__.defaults(this));
      };

      return Game;

    })(BaseModel);
  });

}).call(this);
