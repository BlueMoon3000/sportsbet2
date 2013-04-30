(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  define(["app", "backbone"], function(App, Backbone) {
    var BaseCollection, _ref;

    return App.Collections.BaseCollection = BaseCollection = (function(_super) {
      __extends(BaseCollection, _super);

      function BaseCollection() {
        _ref = BaseCollection.__super__.constructor.apply(this, arguments);
        return _ref;
      }

      BaseCollection.prototype.parse = function(response) {
        return response.response;
      };

      return BaseCollection;

    })(Backbone.Collection);
  });

}).call(this);
