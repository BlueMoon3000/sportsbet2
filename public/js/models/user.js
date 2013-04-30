(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  define(["app", "../models/base", "jquery", "underscore", "backbone"], function(App, BaseModel, $, _, Backbone) {
    var AppUser, _ref;

    return App.Models.User = AppUser = (function(_super) {
      var modelClass;

      __extends(AppUser, _super);

      function AppUser() {
        _ref = AppUser.__super__.constructor.apply(this, arguments);
        return _ref;
      }

      modelClass = AppUser.constructor.name.toLowerCase();

      AppUser.prototype.urlRoot = 'http://local.host:8000/api/v1/appuser/';

      AppUser.prototype.defaults = function() {
        return _.extend(this.constructor.__super__.defaults(this), {
          id: 'findOne',
          email: null,
          fb_user_id: null,
          fb_access_token: null
        });
      };

      AppUser.prototype.is_authenticated = function() {
        return fb_user_id && fb_access_token;
      };

      AppUser.prototype.fb_sync = function(data) {
        return this.set({
          fb_user_id: data.id,
          full_name: data.name,
          first_name: data.first_name,
          last_name: data.last_name,
          email: data.email
        });
      };

      return AppUser;

    })(BaseModel);
  });

}).call(this);
