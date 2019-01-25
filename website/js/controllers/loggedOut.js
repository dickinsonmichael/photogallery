angular.module("photoGallery.loggedOut", ["photoGallery.authService"])
    .controller("loggedOutController", function($scope, $location, authService) {
    console.log("loggedOut.js")

    $scope.changeView = function(view){
        $location.path(view);
    };

    //calling the sign-in method from AuthService to sign in the user to the application
    $scope.login = function(user, isValid) {

        if (isValid) {
            authService.signin(user).then(function(result) {
                console.log("Id Token: " + result.getIdToken().getJwtToken());
                $('.modal-backdrop').remove()
                $location.path("/loggedIn");
            }, function(msg) {
                console.log(msg);
                if ($scope.$$phase != "$digest") {
                    $scope.$apply();
                }
                return;
            });
        } else {
            console.log("Probably you have provided invalid login fields");

        }
    };


});
