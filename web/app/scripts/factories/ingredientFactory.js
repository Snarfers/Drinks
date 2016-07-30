(function() {
  'use strict';

  angular.module('drinksApp')
    .factory('IngredientFactory', function ($scope, $http) {

      this.submitIngredient = function(ingredient){
        return $http.post("http://127.0.0.1:5000/api/ingredient/create", ingredient);
      };

      this.getAllIngredients = function() {
        return $http.get("http://127.0.0.1:5000/api/ingredient/all");
      };

    })
})();
