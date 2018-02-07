var app = angular.module('toDo', []);
app.controller('toDoController', function($scope, $http){
     $http.get('/todo/api/').then(function(response){
          $scope.todoList = [];
          for (var i=0; i< response.data.length; i++){
               var todo = {};
               todo.todoTask = response.data[i].Task
               todo.Done = response.data[i].Done
               todo.id = response.data[i].id
               $scope.todoList.push(todo);
          }
     });

     $scope.todoAdd = function(){
          $scope.todoList.push({todoTask: $scope.todoInput, Done: false});
          $scope.todoInput = '';
     }

     $scope.saveData = function(){
          var data = '/todo/api/',data = {Task: $scope.todoInput, Done: false};
          $http.put('/todo/api/', data)
     };

     $scope.remove = function(){
          var doneList = $scope.todoList;
          $scope.todoList = [];
          angular.forEach(doneList, function(todo){
               if (todo.Done){
                    $http.delete('/todo/api/'+todo.id+'/');
               }
               else {$scope.todoList.push(todo);
               }
          })

     }

})