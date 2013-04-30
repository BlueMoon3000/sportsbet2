(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  define(["app", "models", "jquery", "underscore", "backbone", "../home/match", "text!/templates/home/home.html"], function(App, Models, $, _, Backbone, MatchView, homeTemplate) {
    var homeView, _ref;

    return homeView = (function(_super) {
      __extends(homeView, _super);

      function homeView() {
        _ref = homeView.__super__.constructor.apply(this, arguments);
        return _ref;
      }

      homeView.prototype.events = {
        "click button.create-game": "createMatch",
        "keyup input.game-code": "retrieveMatch",
        "click input.game-code-submit": "retrieveMatch"
      };

      homeView.prototype.retrieveMatch = function(event) {
        var code, match;

        if (event.type !== 'keyup' || event.type === 'keyup' && event.keyCode === 13) {
          code = this.$('.game-code').val() || null;
          match = new Models.Match({
            id: 'findOne'
          });
          return match.fetch({
            data: {
              code: code
            },
            processData: true,
            success: function(model, response) {
              var error, matchView;

              error = null;
              if (response.error && response.error.code === 1) {
                error = 'No match was found with the given code, try starting a new game instead.';
                match = null;
              }
              matchView = new MatchView({
                el: this.$('.match-container'),
                model: match,
                error: error
              });
              return matchView.render();
            },
            error: function(model, response) {
              return console.log(response);
            }
          });
        }
      };

      homeView.prototype.createMatch = function() {
        var match;

        match = new App.Models.Match;
        match.set({
          player_id: App.State.User.id
        });
        return match.save({}, {
          success: function(model, response) {
            var matchView;

            matchView = new MatchView({
              el: this.$('.match-container'),
              model: match,
              error: null
            });
            return matchView.render();
          },
          error: function(model, response) {
            return console.log(response);
          }
        });
      };

      homeView.prototype.render = function() {
        return $(this.el).append(_.template(homeTemplate, {
          user: App.State.User.toJSON()
        }));
      };

      return homeView;

    })(Backbone.View);
  });

}).call(this);
