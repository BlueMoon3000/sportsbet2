(function() {
  define([], function() {
    var App, CONF;

    if (window.ENVIRON === 'dev') {
      CONF = {
        FB_APP_ID: '494835607253773',
        ROOT_URL: 'http://local.host:8000/'
      };
    } else if (window.ENVIRON === 'staging') {
      CONF = {
        FB_APP_ID: '138543369667363',
        ROOT_URL: 'http://sportsbet2.herokuapp.com/'
      };
    }
    App = window.App || {
      Config: CONF,
      Collections: {},
      Models: {},
      Views: {},
      State: {},
      Routers: {}
    };
    window.App = App;
    return App;
  });

}).call(this);
