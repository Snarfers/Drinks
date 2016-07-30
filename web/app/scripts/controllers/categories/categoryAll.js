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
    .controller('CategoryAllController', function ($scope, $http) {

      this.getAllCategories = function(){
        $http.get("http://127.0.0.1:5000/api/category/all").then(function(result){
          $scope.categories = result.data;
        }, function(error){
          console.log("Could not get all ingredients.")

        })
      };

      this.init = function(){
        $http.defaults.useXDomain = true;

        this.getAllCategories();

      }

      this.init();
    });

})();

