var app = angular.module('drinks', ['ngRounter']);

app.config(function($stateProvider, $urlRouterProvider){
    $stateProvider.state('ingredientListing', {
        url: '/ingredient/all',
        templateUrl: '/'
        controller: 'IngredientListingController as ingListCtrl'
    });
});