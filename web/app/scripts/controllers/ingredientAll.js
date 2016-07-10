'use strict';

/**
 * @ngdoc function
 * @name drinksApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the drinksApp
 */
angular.module('drinksApp')
  .controller('IngredientAllController', function ($scope, $http, $resource) {

    this.getAllIngredients = function(){
      $http.get("http://127.0.0.1:5000/api/ingredient/all").then(function(result){
        $scope.ingredients = result.data
        console.log($scope.ingredients);
      }, function(error){

      })
    };

    this.init = function(){
      $http.defaults.useXDomain = true;

      this.getAllIngredients();

    }

    this.init();
  });
