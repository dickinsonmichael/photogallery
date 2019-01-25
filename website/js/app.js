angular.module("photoGallery", ["ngRoute", "photoGallery.authService", "photoGallery.loggedIn", "photoGallery.loggedOut", "photoGallery.profile"])

.config(function($routeProvider) {
    $routeProvider
        .when("/", {
            templateUrl: "js/views/loggedOut.html",
            controller: "loggedOutController"
        })
        .when("/loggedIn", {
            templateUrl: "js/views/loggedIn.html",
            controller: "loggedInController"
        })
        .when("/profile", {
            templateUrl : "js/views/profile.html",
            controller: "profileController"
        })
});