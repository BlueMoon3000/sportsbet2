(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  define(["app", "jquery", "underscore", "backbone", "../models/base"], function(App, $, _, Backbone, BaseModel) {
    var Match, _ref;

    return App.Models.Match = Match = (function(_super) {
      var modelClass;

      __extends(Match, _super);

      function Match() {
        _ref = Match.__super__.constructor.apply(this, arguments);
        return _ref;
      }

      modelClass = Match.constructor.name.toLowerCase();

      Match.prototype.urlRoot = App.Config.ROOT_URL + 'api/v1/match/';

      Match.prototype.defaults = function() {
        return _.extend(this.constructor.__super__.defaults(this));
      };

      return Match;

    })(BaseModel);
  });

}).call(this);
