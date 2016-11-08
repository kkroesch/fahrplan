define('app',["exports", "./bookmark"], function (exports, _bookmark) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.App = undefined;

  function _classCallCheck(instance, Constructor) {
    if (!(instance instanceof Constructor)) {
      throw new TypeError("Cannot call a class as a function");
    }
  }

  var App = exports.App = function () {
    function App() {
      _classCallCheck(this, App);

      this.heading = "Bookmarks";
      this.bookmarks = [];
    }

    App.prototype.addBookmark = function addBookmark() {
      if (this.startStation && this.destinationStation) {
        this.bookmarks.push(new _bookmark.Bookmark(this.startStation, this.destinationStation));
      }
    };

    App.prototype.removeBookmark = function removeBookmark(bookmark) {
      var index = this.bookmarks.indexOf(bookmark);
      if (index !== -1) {
        this.bookmarks.splice(index, 1);
      }
    };

    App.prototype.nextConnection = function nextConnection() {
      console.log("Triggered");
    };

    return App;
  }();
});
define('bookmark',["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });

  function _classCallCheck(instance, Constructor) {
    if (!(instance instanceof Constructor)) {
      throw new TypeError("Cannot call a class as a function");
    }
  }

  var Bookmark = exports.Bookmark = function Bookmark(start, destination) {
    _classCallCheck(this, Bookmark);

    this.start = start;
    this.destination = destination;
  };
});
define('environment',["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = {
    debug: true,
    testing: true
  };
});
define('main',['exports', './environment'], function (exports, _environment) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.configure = configure;

  var _environment2 = _interopRequireDefault(_environment);

  function _interopRequireDefault(obj) {
    return obj && obj.__esModule ? obj : {
      default: obj
    };
  }

  Promise.config({
    warnings: {
      wForgottenReturn: false
    }
  });

  function configure(aurelia) {
    aurelia.use.standardConfiguration().feature('resources');

    if (_environment2.default.debug) {
      aurelia.use.developmentLogging();
    }

    if (_environment2.default.testing) {
      aurelia.use.plugin('aurelia-testing');
    }

    aurelia.start().then(function () {
      return aurelia.setRoot();
    });
  }
});
define('resources/index',["exports"], function (exports) {
  "use strict";

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.configure = configure;
  function configure(config) {}
});
define('text!app.html', ['module'], function(module) { module.exports = "\n<template>\n  <h1>${heading}</h1>\n\n  <form class=\"form-inline\" submit.trigger=\"addBookmark()\">\n    <div class=\"form-group\">\n      <label>Von</label>\n      <input type=\"text\" class=\"form-control\" value.bind=\"startStation\">\n    </div>\n    <div class=\"form-group\">\n      <label>Nach</label>\n      <input type=\"text\" class=\"form-control\" value.bind=\"destinationStation\">\n    </div>\n    <button class=\"btn btn-default\" type=\"submit\">Bookmark</button>\n  </form>\n\n  <p></p>\n\n  <ul class=\"list-group\">\n    <li class=\"list-group-item\" repeat.for=\"bookmark of bookmarks\" click.trigger=\"nextConnection(bookmark)\">\n      <button type=\"button\" class=\"close\" aria-label=\"Delete\" click.trigger=\"removeBookmark(bookmark)\">\n        <i class=\"fa fa-trash\" aria-hidden=\"true\"></i>\n      </button>\n      <button type=\"button\">\n        <i class=\"fa fa-train\" aria-hidden=\"true\"></i>\n      </button>\n      Von ${bookmark.start} Nach ${bookmark.destination}\n    </li>\n  </ul>\n</template>"; });
//# sourceMappingURL=app-bundle.js.map