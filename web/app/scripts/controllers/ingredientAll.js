'use strict';

/**
 * @ngdoc function
 * @name drinksApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the drinksApp
 */
angular.module('drinksApp')
  .controller('IngredientAllController', function ($scope) {

      this.init = function(){
          $scope.someData = [];
      }

      this.init();
  });
