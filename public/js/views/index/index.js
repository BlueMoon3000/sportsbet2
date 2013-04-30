(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  define(["app", "models", "collections", "jquery", "underscore", "backbone", "facebook", "text!/templates/index/index.html"], function(App, Models, Collections, $, _, Backbone, FB, indexTemplate) {
    var indexView, _ref;

    return indexView = (function(_super) {
      __extends(indexView, _super);

      function indexView() {
        _ref = indexView.__super__.constructor.apply(this, arguments);
        return _ref;
      }

      indexView.prototype.events = {
        "click a.facebook-login": "login"
      };

      indexView.prototype.render = function() {
        return $(this.el).append(_.template(indexTemplate));
      };

      indexView.prototype.remove = function() {
        return $(this.el).empty();
      };

      indexView.prototype.login = function() {
        return FB.login(function(response) {
          if (response.authResponse) {
            return FB.api('/me', function(response) {
              var user;

              user = new Models.User;
              user.fb_sync(response);
              return user.getOrCreate({
                fb_user_id: response.id
              }, {
                success: function(model, response) {
                  console.log('Good to see you ' + user.get('first_name') + '.');
                  App.Collections.Users.add(user);
                  App.State.User = user;
                  return App.Routers.Router.navigate('home', true);
                },
                error: function(model, response) {
                  return console.log(response);
                }
              });
            });
          } else {
            return console.log('User cancelled.');
          }
        }, {
          scope: 'email'
        });
      };

      return indexView;

    })(Backbone.View);
  });

}).call(this);
