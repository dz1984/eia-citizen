/**
 * Requirements:
 * - $.position()
 * - <script type="text/javascript" src="//maps.googleapis.com/maps/api/js?sensor=false"></script>
 */
(function($) {

	var methods = {

		/**
		 * init
		 */
		init: function(settings) {
			$(this).css("display", "none");
			$(this).css("position","absolute");
			$(this).css("margin", "0");
			$(this).css("border","1px solid #777");
			$(this).css("padding", "5px 10px");
			$(this).css("background","#fff");
			$(this).css("z-index","10");
			$(this).width(400);
			$(this).height(300);

			var that = this;
			var _canvasId = "geocoding_mapcanvas";
			var _okId = "geocoding_ok";
			var _html = "";
			//_html  = '地名約略定位：<input type="text" value="大湖公園" />';
			//_html = '<input type="button" value="Go" />';
			_html += '<div id="{CANVAS_ID}"></div>'.replace("{CANVAS_ID}", _canvasId);
			_html += '<button id="{OK_ID}">好了!</button>'.replace("{OK_ID}", _okId);
			$(this).append(_html);
			$("#"+_canvasId).width(400);
			$("#"+_canvasId).height(260);
			$("#"+_canvasId).css("border", "1px solid red");
			$("#"+_okId).on("click", function() { $(that).geocoding("close"); });

			// Google Maps API v3
			var mapOptions = {
				center: new google.maps.LatLng(settings.lat, settings.lng),
				zoom: 16,
				mapTypeId: google.maps.MapTypeId.ROADMAP
			};
			var map = new google.maps.Map(document.getElementById(_canvasId), mapOptions);
			google.maps.event.addListener(map, "center_changed", function() {
				var pos = map.getCenter();
				$(settings.lat_field).val(pos.lat().toFixed(5));
				$(settings.lng_field).val(pos.lng().toFixed(5));
			});
		},

		/**
		 * open
		 */
		open: function(where) {
			var pos = $(where).position();
			$(this).css("left", pos.left);
			$(this).css("top" , pos.top + $(where).height()+3);
			$(this).css("display", "block");
		},

		/**
		 * close
		 */
		close: function() {
			$(this).css("display", "none");
		}

	};

	$.fn.geocoding = function(method) {
		var msg;
		if (this.length==1) {
			if (methods[method]) {
				return methods[method].apply(this, Array.prototype.slice.call(arguments,1));
			} else if (typeof(method)==='object' || !(method)) {
				return methods["init"].apply(this, arguments);
			} else {
				msg = "No such method {METHOD}".replace("{METHOD}", method);
			}
		} else {
			msg = "$.geocoding can apply only one element.";
		}
		console.error(msg);
	};

})($);
