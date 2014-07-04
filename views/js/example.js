(function() {

  var margin = {
    top: 40,
    right: 20,
    bottom: 30,
    left: 40
  };

  var all_width = 960,
      all_height = 500,
      width = all_width - margin.left - margin.right,
      height = all_height - margin.top - margin.bottom;


  var getXRange = function(dataset) {
    return d3.scale.ordinal()
        .rangeRoundBands([0, width], 0.1)
        .domain(dataset.map(function(d) {
                  return d.devunit;
        }));
  };

  var getYRange = function(dataset) {
    return d3.scale.linear()
          .range([height, 0])
          .domain([0, d3.max(dataset, function(d) {
                    return d.count;
            })
          ]);
  };

  var getXAxis = function(xRange) {
    return d3.svg.axis()
          .scale(xRange)
          .tickSize(5)
          .tickSubdivide(true);
  };

  var getYAxis = function(yRange) {
    return  d3.svg.axis()
            .scale(yRange)
            .tickSize(5)
            .orient("left")
            .tickSubdivide(true);
  };

  var wrap = function(text, width) {
    text.each(function() {
      var text = d3.select(this),
      words = text.text().split(/(?:)/).reverse(),
      line = [],
      lineNumber = 0,
      y = text.attr("y"),
      lineHeight = 2,
      dy = parseFloat(text.attr("dy")),
      tspan = text.text(null).append("tspan").attr("x", 0).attr("y", y).attr("dy", dy + "em");


      while (word = words.pop()) {
        line.push(word);
        tspan.text(line.join(" "));
        if (tspan.node().getComputedTextLength() > width) {
          line.pop();
          tspan.text(line.join(" "));
          line = [word];
          tspan = text.append("tspan").attr("x", 0).attr("y", y).attr("dy", ++lineNumber * lineHeight + dy + "em").text(word);
        }
      }
    });
  };

  var generateBarChart = function(JSONData,elementId) {
    var dataset = JSONData.slice();

    var xRange = getXRange(dataset);

    var yRange = getYRange(dataset);

    var xAxis = getXAxis(xRange);
    
    var yAxis = getYAxis(yRange);

    var svg = d3.select(elementId)
              .append("svg")
              .attr("width", all_width)
              .attr("height", all_height)
              .append("g")
              .attr("transform", "translate(40,40)");

     svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
      .selectAll(".tick text")
      .call(wrap, xRange.rangeBand());

      svg.append("g")
      .attr("class", "y axis")
      .call(yAxis);

      svg.selectAll(".bar")
      .data(dataset)
      .enter()
      .append("rect")
      .attr("class", "bar")
      .attr("x", function(d) {
        return xRange(d.devunit);
      })
      .attr("y", function(d) {
        return yRange(d.count);
      })
      .attr("width", xRange.rangeBand())
      .attr("height", function(d) {
        return height - yRange(d.count);
      });
  };

  d3.json('/api/summary/dev/send', function(JSONData) {
    generateBarChart(JSONData,"#example_dev_send");
  });

  d3.json('/api/summary/dev/pass', function(JSONData) {
    generateBarChart(JSONData,"#example_dev_pass");
  });

}).call(this);