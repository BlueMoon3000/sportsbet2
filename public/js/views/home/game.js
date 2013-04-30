(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  define(["app", "models", "jquery", "underscore", "backbone", "text!/templates/home/game.html"], function(App, Models, $, _, Backbone, gameTemplate) {
    var gameView, _ref;

    gameView = (function(_super) {
      __extends(gameView, _super);

      function gameView() {
        _ref = gameView.__super__.constructor.apply(this, arguments);
        return _ref;
      }

      gameView.prototype.events = {
        "click a.team-select": "submitPick"
      };

      gameView.prototype.initialize = function() {
        return this.options.picks.bind('add', this.render, this);
      };

      gameView.prototype.submitPick = function(event) {
        var pick, team_id;

        event.preventDefault();
        if ($(event.currentTarget).hasClass('away')) {
          team_id = this.model.get('away').id;
        } else {
          team_id = this.model.get('home').id;
        }
        pick = new Models.Pick({
          player_id: App.State.User.id,
          match_id: this.options.match.id,
          team_id: team_id,
          game_id: this.model.id
        });
        console.log(pick);
        pick.save();
        return this.options.picks.add(pick);
      };

      gameView.prototype.render = function() {
        var picks;

        $(this.el).empty();
        picks = null;
        if (this.options.picks.length !== 0) {
          picks = this.options.picks.toJSON();
        }
        return $(this.el).append(_.template(gameTemplate, {
          _: _,
          game: this.model.toJSON(),
          picks: _.where(picks, {
            game_id: this.model.id
          })
        }));
      };

      return gameView;

    })(Backbone.View);
    return gameView;
  });

}).call(this);
