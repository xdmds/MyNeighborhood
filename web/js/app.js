angular.module('myneighborhood', ['ui.bootstrap', 'ui.utils', 'nvd3', 'google-maps'])
.factory('_', ['$window', function($window){
	return $window._;
}])
.controller('homeCtrl', ['$scope', '_', function($scope, $http, _) {
	$scope.map = {
		center: {
			latitude: 40.7127,
			longitude: -74.0059
		},
		zoom: 11,
		heatLayerCallback: function (layer) {
        	var mockHeatLayer = new MockHeatLayer(layer);
      	}
	};
	$scope.zip;

	var latlng =  new google.maps.LatLng(37.797847, -122.429388);
	console.log(latlng);
	
	//console.log(GoogleMapApi);
	/*
	GoogleMapApi.then(function(maps) {
		console.log("GOT MAPS");
	});
*/
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(function(position) {
			//console.log(GoogleMapApi);
			$scope.$apply(function() {
				$scope.map.center = position.coords;
				$scope.map.zoom = 14;
				//$scope.getzip();
				console.log(position.coords);
			});
		});
	}
}]);
