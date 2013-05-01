define [], () -> 
  # This serves as a state object for the entire app.
  if window.ENVIRON == 'dev'
    CONF = 
      FB_APP_ID: '494835607253773'
      ROOT_URL: 'http://local.host:5000/'
  else if window.ENVIRON == 'staging'
    CONF = 
      FB_APP_ID: '138543369667363'
      ROOT_URL: 'http://sportsbet2.herokuapp.com/'

  App = window.App or 
    Config: CONF
    Collections: {}
    Models: {}
    Views: {}
    State: {}
    Routers: {}

  window.App = App
  return App