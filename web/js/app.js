angular.module('myneighborhood', ['ui.bootstrap', 'ui.utils', 'nvd3', 'google-maps'])
.factory('_', ['$window', function($window){
	return $window._;
}])
.controller('homeCtrl', ['$scope', '$http', '_', function($scope, $http, _) {
	$scope.heatmaplayer;
	$scope.complaintData;
	$scope.map = {
		center: {
			latitude: 40.7127,
			longitude: -74.0059
		},
		zoom: 11,
		heatLayerCallback: function (layer) {
        	$scope.heatmaplayer = layer;
      	}
	};
	$scope.chartoptions = {
		"chart": {
			"type": "pieChart",
			"height": 500,
			"x": function(d){return d.key;},
            "y": function(d){return d.y;},
            "showLegend": false,
            "transitionDuration": 500
		}
	}
	$scope.piedata = []
	$scope.position;
	$scope.zipcode = "";
	$scope.category;
	$scope.categories = [];
	$scope.$watch('zipcode', function(newValue, oldValue) {
		console.log("NEW ZIPCODE: " + newValue);
		if (newValue.length == 5){
			$http.post('http://localhost:8001/api/categories/',{"zipcode": $scope.zipcode})
			.success(function(data) {
				$scope.categories = data['type_set'];
				$scope.piedata = data['pie_data']
				console.log($scope.piedata);
			});
		}
	});
	$scope.getComplaintData = function(cat){
		$scope.category = cat;
		console.log("NEW CATEGORY " + $scope.category);
		if ($scope.category.length > 0) {
			console.log("SENDING COMPLAINT DATA REQUEST");
			$http.post('http://localhost:8001/api/complaints/', {
				"zipcode": $scope.zipcode,
				"complaint_type": $scope.category
			}).success(function(data) {
				$scope.complaintData = data;
				console.log($scope.complaintData);
				var latlngdata = []
				_.forEach($scope.complaintData, function(coordinate) {
					latlngdata.push(new google.maps.LatLng(coordinate[0], coordinate[1]));
				});
				var heatArray = new google.maps.MVCArray(latlngdata);
				$scope.heatmaplayer.setData(heatArray);
			});
		}
	};
	$scope.$watch('map', function(newValue, oldValue) {
		console.log("NEW CENTER");
	}, true)
	$scope.$watch('position', function(newValue, oldValue) {
		console.log("NEW VALUE");
		console.log(newValue);
		if (newValue) {
		$http.get('http://ws.geonames.org/findNearbyPostalCodesJSON', {
			params: { "formatted" : "true",
				"lat": $scope.position.latitude,
				"lng": $scope.position.longitude,
				"username": "rrelasmar"
			}}).success(function(data) {
				var ziplocation = data.postalCodes[0];
				$scope.zipcode = ziplocation['postalCode'];
			});
		}
	}, true);
	$scope.testFunction = function() {
		console.log("TEST!");
	}

	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(function( position) {
			$scope.$apply(function() {
				$scope.map.center = position.coords;
				$scope.map.zoom = 15;
				console.log(position.coords);
				$scope.position = position.coords;
			});
		});
	}
}]);
