(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  define(["app", "models", "collections", "jquery", "underscore", "backbone", "facebook", "text!/templates/base/base.html"], function(App, Models, Collections, $, _, Backbone, FB, baseTemplate) {
    var baseView, _ref;

    return baseView = (function(_super) {
      __extends(baseView, _super);

      function baseView() {
        _ref = baseView.__super__.constructor.apply(this, arguments);
        return _ref;
      }

      baseView.prototype.render = function() {
        return $(this.el).append(_.template(baseTemplate));
      };

      return baseView;

    })(Backbone.View);
  });

}).call(this);
