(function() {
  define([], function() {
    var App;

    App = window.App || {
      Config: {
        FB_APP_ID: '494835607253773'
      },
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
