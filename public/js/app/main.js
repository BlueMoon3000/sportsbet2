(function() {
  define(["app", "router", "backbone", "facebook", "../views/base/base"], function(App, Router, Backbone, FB, BaseView) {
    var init;

    init = function() {
      var AppView;

      FB.init({
        appId: App.Config.FB_APP_ID,
        status: true,
        cookie: true,
        xfbml: true
      });
      $(document).on('click', 'a:not([data-bypass])', function(event) {
        var href, protocol;

        href = $(this).attr('href');
        protocol = this.protocol + '//';
        if (href && href.slice(0, protocol.length !== protocol && href.indexOf('javascript:' !== 0))) {
          event.preventDefault();
          return Backbone.history.navigate(href, true);
        }
      });
      AppView = new BaseView();
      App.State.BaseView = AppView;
      return Router.init();
    };
    return {
      init: init
    };
  });

}).call(this);
