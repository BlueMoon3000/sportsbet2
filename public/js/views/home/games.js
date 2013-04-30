(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  define(["app", "models", "jquery", "underscore", "backbone", "../home/game"], function(App, Models, $, _, Backbone, GameView) {
    var gamesView, _ref;

    gamesView = (function(_super) {
      __extends(gamesView, _super);

      function gamesView() {
        _ref = gamesView.__super__.constructor.apply(this, arguments);
        return _ref;
      }

      gamesView.prototype.initialize = function() {
        var self;

        this.listenTo(App.Collections.Games, 'add', this.addOne);
        this._childViews = [];
        self = this;
        this.picks = new App.Collections.Picks;
        this.picks.fetch({
          data: {
            match_id: this.options.match.id
          },
          processData: true,
          success: function(collection, response) {
            return self.collection.fetch({
              success: function(collection, response) {
                return console.log(collection, response);
              },
              error: function() {
                return console.log('hi');
              }
            });
          }
        });
        setInterval(function() {
          return self.updatePicks();
        }, 5000);
        return this.picks.bind('add', this.update, this);
      };

      gamesView.prototype.updatePicks = function() {
        return this.picks.fetch({
          data: {
            match_id: this.options.match.id
          },
          processData: true,
          update: true
        });
      };

      gamesView.prototype.addOne = function(game) {
        var gameView;

        gameView = new GameView({
          model: game,
          picks: this.picks,
          match: this.options.match
        });
        gameView.render();
        this._childViews.push(gameView);
        return this.$el.append(gameView.el);
      };

      gamesView.prototype.update = function() {
        return console.log(this.picks);
      };

      return gamesView;

    })(Backbone.View);
    return gamesView;
  });

}).call(this);
