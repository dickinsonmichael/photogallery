angular.module("photoGallery.profile", ["photoGallery.authService"])
    .controller("profileController", function($scope, $location, authService) {
        console.log("profile.js")

        if (true) {
                authService.isAuthenticated().then(function(result) {
                    console.log("User is authenticated: " + result);
                    if(result === false) {
                        console.log("Redirecting to login page")
                        $location.path('/');
                    }
                    authService.getUserInfo().then(function(result) {
                    console.log(result)
                    $scope.user = result
                    return
                    })
                }, function(msg) {
                    console.log(msg);
                    $scope.errormessage = "Unable to access DynamoDB";

                    if ($scope.$$phase != '$digest') {
                        $scope.$apply();
                    }
                    return;
                });
            } else {
                $scope.errormessage = "Some error happened";

            };

        $scope.status="";

        $scope.logout = function() {
            authService.logOut();
            $location.path('/');
        }

    });
