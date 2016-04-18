var express = require('express');
var http = require('http');
var PythonShell = require('python-shell');
var ut = require('date-utils');

var app = express();

app.use( express.static(__dirname));

app.get('/', function(req, res) {

	return res.sendFile(__dirname + '/Design/pages/Dashboardpage.html');
    //return res.sendFile(__dirname + '/indi.html');

});




app.get('/query1' , function(req, res) {

  var DS_type = req.param('v6'); 
  var page_type = req.param('v7'); 


  if(page_type == "CSV")
  { 
      var row_1 = req.param('d');  
   var header = req.param('h'); 
   
   var options = {
      //mode: 'text',
      args: [DS_type, page_type, row_1.split(','), header.split(',')]
   };

   PythonShell.run('abc.py', options, function (err, results) {
     if (err) throw err;
    // results is an array consisting of messages collected during execution
    console.log(results)
    output = JSON.parse(results);
    var scoredLabels = output.Results.output1.value.Values[0][0];
    var scoreProb = output.Results.output1.value.Values[0][1];
    var scoreProb = 0;

    console.log('POP %j', output);
    res.send(row_1+','+scoredLabels+','+scoreProb);

  });

  }
  else
  {
      var header = ["Account", "variable", "df$date", "df$month"];
      var acc = req.param('v1'); 
      var variable = req.param('v2'); 
      //var kw = req.param('v3'); 
      var d = req.param('v4'); 
      var mnth = req.param('v5'); 

      var valuess = new Array();
      valuess.push(acc);
      valuess.push(variable);
      //valuess.push(kw);
      valuess.push(d);
      valuess.push(mnth);

    var options = {
      //mode: 'text',
      //args: [type, header, acc, variable, kw, d, mnth]
      args: [DS_type, page_type, header, valuess]
    };

    PythonShell.run('abc.py', options, function (err, results) {
      if (err) throw err;
    // results is an array consisting of messages collected during execution
    //console.log(results)
    output = JSON.parse(results);
    var scoredLabels = output.Results.output1.value.Values[0][0];
    //var scoreProb = output.Results.BostonPropertyOutput.value.Values[0][1];
    //var scoreProb = 0;

   // console.log('POP %j', output);
    //res.send(scoredLabels+','+scoreProb);
    res.send(scoredLabels);
    
  });
  
  }

});


http.createServer(app).listen(4030, function() {
	console.log("LOADED SERVER");
});