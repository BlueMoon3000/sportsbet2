define [], () -> 
  # This serves as a state object for the entire app.
  App = window.App or 
    Config: # Global Config
      FB_APP_ID: '494835607253773'
    Collections: {}
    Models: {}
    Views: {}
    State: {}
    Routers: {}

  window.App = App
  return App