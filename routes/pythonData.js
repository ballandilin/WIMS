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
  //           // py(img, res);
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
  console.log("envoie de l'image")
  var results = [];

  myscript.on('message', function(message) {
    console.log(message);
    results.push(message);
  });


  myscript.end(function(err, code, signal) {    
    if (err) {
      console.log("erruer");
      console.log(err);
      throw err
    };
    console.log(results);
    res.io.emit("result", results[1]);            
  });


//   let options = {
//     mode: 'text',
//     pythonOptions: ['-u'], // get print results in real-time
//     scriptPath: 'public/compare',
//     args: [img]
// };

  

//   PythonShell.run('main.py', options, function (err, results) {
//     if (err) throw err;
//     // results is an array consisting of messages collected during execution
//     // req.session.img = results[0];
//     res.io.emit("result", results[1]);
//     // res.render('index', { title: 'WIMS', name: results[0]});
//     console.log('results: %j', results[1]);
// });

  // pyshell.on('message', function (message) {
  //   // received a message sent from the Python script (a simple "print" statement)
  //   console.log(message);

  // });

  // // end the input stream and allow the process to exit
  // pyshell.end(function (err,code,signal) {
  //   if (err) throw err;
  //   console.log('The exit code was: ' + code);
  //   console.log('The exit signal was: ' + signal);
  //   console.log('finished');
  // });

  // res.render('index', { title: 'WIMS'});
}