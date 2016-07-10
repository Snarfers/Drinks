'use strict';

/**
 * @ngdoc function
 * @name drinksApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the drinksApp
 */
angular.module('drinksApp')
  .controller('IngredientCreateController', function ($scope, $http) {

    $scope.submitIngredient = function(){
      $http.post("http://127.0.0.1:5000/api/ingredient/create", $scope.ingredient).then(function(result){
        console.log("Successfully submitted Ingredient");
      }, function(error){
        console.log("Unsuccessfully submitted Ingredient");
      })
    };

    this.init = function(){
      $http.defaults.useXDomain = true;

      $scope.ingredient = {};

    }

    this.init();
  });
