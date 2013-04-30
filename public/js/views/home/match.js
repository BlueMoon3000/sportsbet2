(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  define(["app", "models", "jquery", "underscore", "backbone", "../home/games", "text!/templates/home/match.html"], function(App, Models, $, _, Backbone, GamesView, matchTemplate) {
    var matchView, _ref;

    matchView = (function(_super) {
      __extends(matchView, _super);

      function matchView() {
        _ref = matchView.__super__.constructor.apply(this, arguments);
        return _ref;
      }

      matchView.prototype.render = function() {
        var gamesView, match;

        $(this.el).empty();
        match = null;
        if (this.model) {
          match = this.model.toJSON();
        }
        $(this.el).append(_.template(matchTemplate, {
          match: match,
          error: this.options.error
        }));
        if (this.model) {
          return gamesView = new GamesView({
            el: this.$('.games-container'),
            match: this.model,
            collection: App.Collections.Games
          });
        }
      };

      return matchView;

    })(Backbone.View);
    return matchView;
  });

}).call(this);
