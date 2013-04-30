(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  define(["app", "models", "jquery", "underscore", "backbone", "../collections/base"], function(App, Models, $, _, Backbone, BaseCollection) {
    var Picks, _ref;

    Picks = (function(_super) {
      __extends(Picks, _super);

      function Picks() {
        _ref = Picks.__super__.constructor.apply(this, arguments);
        return _ref;
      }

      Picks.prototype.model = Models.Pick;

      Picks.prototype.url = '/api/v1/pick/';

      Picks.prototype.urlRoot = 'http://local.host:8000' + Picks.url;

      return Picks;

    })(BaseCollection);
    return App.Collections.Picks = Picks;
  });

}).call(this);
