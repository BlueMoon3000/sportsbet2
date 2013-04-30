(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  define(["app", "jquery", "underscore", "backbone", "../views/index/index", "../views/home/home"], function(App, $, _, Backbone, indexView, homeView) {
    var AppRouter, init, _ref;

    AppRouter = (function(_super) {
      __extends(AppRouter, _super);

      function AppRouter() {
        _ref = AppRouter.__super__.constructor.apply(this, arguments);
        return _ref;
      }

      AppRouter.prototype.routes = {
        "": "index",
        "home": "home"
      };

      AppRouter.prototype.navigate = function() {
        $(App.State.currentView.el).empty();
        App.State.currentView.unbind();
        App.State.currentView = null;
        return AppRouter.__super__.navigate.apply(this, arguments);
      };

      AppRouter.prototype.index = function() {
        var index;

        index = new indexView({
          el: App.State.BaseView.elChild
        });
        return this.render(index);
      };

      AppRouter.prototype.home = function() {
        var home;

        home = new homeView({
          el: App.State.BaseView.elChild
        });
        return this.render(home);
      };

      AppRouter.prototype.render = function(view) {
        App.State.currentView = view;
        return App.State.currentView.render();
      };

      return AppRouter;

    })(Backbone.Router);
    init = function() {
      App.Routers.Router = new AppRouter;
      return Backbone.history.start({
        pushState: true
      });
    };
    return {
      init: init
    };
  });

}).call(this);
