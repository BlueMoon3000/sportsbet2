define ["app", "jquery", "backbone"], (App, $, Backbone) -> 
  App.Models.BaseModel = class BaseModel extends Backbone.Model
    defaults: (model) ->
        modelClass = model.constructor.name.toLowerCase()
        model: 'core.' + modelClass

    parse: (response) ->
        # Not crazy about this... lets update the backend to make it nicer...
        if response.error
            return null
        if response.response
            return response.response
        else
            return response

    getOrCreate: (data, callback) ->
        self = this
        this.fetch
            data: data
            processData: true
            success: (model, response) ->
                if response.error and response.error.code == 1
                    model.set id:null; # Hack. Nothing found tho, so we reset to null id.
                    model.save {}, 
                        success: (model, response) -> 
                            callback.success model, response 
                        error: (model, response) -> 
                            callback.error model, response
                else if response.response.error
                    callback.error model, response
                else
                    callback.success model, response
            error: (model, response) -> console.log response