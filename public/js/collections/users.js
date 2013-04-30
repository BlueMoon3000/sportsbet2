(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  define(["app", "models", "jquery", "underscore", "backbone", "../collections/base"], function(App, Models, $, _, Backbone, BaseCollection) {
    var Users, _ref;

    Users = (function(_super) {
      __extends(Users, _super);

      function Users() {
        _ref = Users.__super__.constructor.apply(this, arguments);
        return _ref;
      }

      Users.prototype.model = Models.User;

      Users.prototype.url = '/api/v1/appuser/';

      Users.prototype.urlRoot = 'http://local.host:8000' + Users.url;

      return Users;

    })(BaseCollection);
    return App.Collections.Users = new Users;
  });

}).call(this);
