(function() {

  var margin = {
    top: 20,
    right: 20,
    bottom: 120,
    left: 65
  };

  var all_width = 960,
      all_height = 500,
      width = all_width - margin.left - margin.right,
      height = all_height - margin.top - margin.bottom;



  var generateBarChart = function(data,elementId) {
    var svg = dimple.newSvg(elementId, all_width, all_height);
    var myChart = new dimple.chart(svg, data);

    myChart.setBounds(margin.left, margin.top, width, height);

    var x = myChart.addCategoryAxis("x", "devunit"),
    y = myChart.addMeasureAxis("y","count");
    myChart.addSeries(null, dimple.plot.bar);
    myChart.draw();
    x.titleShape.text("開發單位");
    y.titleShape.text("筆數");
  };

  d3.json("/api/summary/dev/send", function(JSONData) {
    generateBarChart(JSONData,"#example_dev_send");
      
  });

  d3.json("/api/summary/dev/pass", function(JSONData) {
    generateBarChart(JSONData,"#example_dev_pass");
  });

}).call(this);