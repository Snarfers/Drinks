(function () {
  'use strict';

  /**
   * @ngdoc overview
   * @name drinksApp
   * @description
   * # drinksApp
   *
   * Main module of the application.
   */
  angular
    .module('drinksApp', [
      'ngAnimate',
      'ngAria',
      'ngCookies',
      'ngMessages',
      'ngResource',
      'ngRoute',
      'ngSanitize',
      'ui.router',
      'ngMaterial'
    ])
    .config(['$routeProvider', '$stateProvider', function ($routeProvider, $stateProvider) {

      $stateProvider.state('ingredientAll', {
        templateUrl: 'views/ingredient/ingredientAll.html',
        controller: 'IngredientAllController as ingredientAllCtrl'
      });

      $stateProvider.state('ingredientCreate', {
        templateUrl: 'views/ingredient/ingredientCreate.html',
        controller: 'IngredientCreateController as ingredientCreateCtrl'
      });

      $stateProvider.state('categoryAll', {
        templateUrl: 'views/category/categoryAll.html',
        controller: 'CategoryAllController as categoryAllCtrl'
      });

      $stateProvider.state('categoryCreate', {
        templateUrl: 'views/category/categoryCreate.html',
        controller: 'CategoryCreateController as categoryCreateCtrl'
      });

    }]);

})();
