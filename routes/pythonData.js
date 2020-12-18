var express = require('express');
var router = express.Router();
var my_lzma = require("lzma");



/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'WIMS'});
});




router.post('/', function(req, res, next) {

  var img = req.body.img;
  console.log("img");
  // my_lzma.compress(img, 9, function on_compress_complete(result) {
  //           console.log("Compressed: " + result.length);
  //           img = result;
  //           py(img, res);
  //       }, function on_compress_progress_update(percent) {
  //           console.log("Compressing: " + (percent * 100) + "%");
  //       });


  py(img, res);
  // res.render('index', { title: 'WIMS'});

  res.send(req.session)
  // res.render('login', { title: 'sketchy' });
});


module.exports = router;


function py(img, res) {

  let {PythonShell} = require('python-shell')

  let options = {
    pythonOptions: ['-u'], // get print results in real-time
    scriptPath: 'public/compare'
};

  myscript = new PythonShell('main.py', options);
  myscript.send(img);
  var results = [];

  myscript.on('message', function(message) {
    res.io.emit("progress", message);
    results.push(message);
  });


  myscript.end(function(err, code, signal) {    
    if (err) {
      // errorHandler(res);
      console.log(err);
      results.push("face not found");
      // throw err
    };
    console.log(results);
    res.io.emit("result", results[0]);            
  });




}