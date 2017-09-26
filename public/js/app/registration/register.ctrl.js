/**
 * Created by graham on 9/24/17.
 */

 (function() {
     'use strict';
 
     angular
         .module('app')
         .controller('RegisterController', RegisterController);
 
    RegisterController.$inject = ['$scope'];
     function RegisterController($scope) {
         var vm = this;
         vm.someValue = "this is the value";
 
         activate();
 
         ////////////////
 
         function activate() { }
     }
 })();