(function(){
  'use strict';

  /**
   * @ngdoc function
   * @name drinksApp.controller:MainCtrl
   * @description
   * # MainCtrl
   * Controller of the drinksApp
   */
  angular.module('drinksApp')
    .controller('CategoryCreateController', function ($scope, $http) {

      $scope.submitCategory = function(){
        $http.post("http://127.0.0.1:5000/api/category/create", $scope.category).then(function(result){
          console.log("Successfully submitted Ingredient");
        }, function(error){
          console.log("Unsuccessfully submitted Ingredient");
        })
      };

      this.init = function(){
        $http.defaults.useXDomain = true;

        $scope.category = {};

      }

      this.init();
    });
})();


