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
    .controller('IngredientAllController', ['$scope', '$http', 'IngredientFactory', function ($scope, $http, IngredientFactory) {

      this.getAllIngredients = function(){
        IngredientFactory.getAllIngredients().then(function(result){
          $scope.ingredients = result.data;
        }, function(error){
          console.log("Could not get all ingredients.")

        })
      };

      this.init = function(){
        $http.defaults.useXDomain = true;

        this.getAllIngredients();

      }

      this.init();
    }]);
})();

