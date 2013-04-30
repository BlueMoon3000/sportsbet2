(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  define(["app", "jquery", "backbone"], function(App, $, Backbone) {
    var BaseModel, _ref;

    return App.Models.BaseModel = BaseModel = (function(_super) {
      __extends(BaseModel, _super);

      function BaseModel() {
        _ref = BaseModel.__super__.constructor.apply(this, arguments);
        return _ref;
      }

      BaseModel.prototype.defaults = function(model) {
        var modelClass;

        modelClass = model.constructor.name.toLowerCase();
        return {
          model: 'core.' + modelClass
        };
      };

      BaseModel.prototype.parse = function(response) {
        if (response.response) {
          return response.response;
        } else {
          return response;
        }
      };

      BaseModel.prototype.getOrCreate = function(data, callback) {
        var self;

        self = this;
        return this.fetch({
          data: data,
          processData: true,
          success: function(model, response) {
            if (response.error && response.error.code === 1) {
              model.set({
                id: null
              });
              return model.save({}, {
                success: function(model, response) {
                  return callback.success(model, response);
                },
                error: function(model, response) {
                  return callback.error(model, response);
                }
              });
            } else if (response.response.error) {
              return callback.error(model, response);
            } else {
              return callback.success(model, response);
            }
          },
          error: function(model, response) {
            return console.log(response);
          }
        });
      };

      return BaseModel;

    })(Backbone.Model);
  });

}).call(this);
