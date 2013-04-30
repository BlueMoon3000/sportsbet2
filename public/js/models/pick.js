(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  define(["app", "jquery", "underscore", "backbone", "../models/base"], function(App, $, _, Backbone, BaseModel) {
    var Pick, _ref;

    return App.Models.Pick = Pick = (function(_super) {
      var modelClass;

      __extends(Pick, _super);

      function Pick() {
        _ref = Pick.__super__.constructor.apply(this, arguments);
        return _ref;
      }

      modelClass = Pick.constructor.name.toLowerCase();

      Pick.prototype.urlRoot = 'http://local.host:8000/api/v1/pick/';

      Pick.prototype.defaults = function() {
        return _.extend(this.constructor.__super__.defaults(this));
      };

      return Pick;

    })(BaseModel);
  });

}).call(this);
