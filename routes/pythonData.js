var express = require('express');
var router = express.Router();



/* GET home page. */
router.get('/', function(req, res, next) {

  let {PythonShell} = require('python-shell')
  // import {PythonShell} from 'python-shell';

  PythonShell.defaultOptions = { scriptPath: 'public\\opencv' };

  let pyshell = new PythonShell('findSimilarity.py');

  pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
    console.log(message);
  });

  // end the input stream and allow the process to exit
  pyshell.end(function (err,code,signal) {
    if (err) throw err;
    console.log('The exit code was: ' + code);
    console.log('The exit signal was: ' + signal);
    console.log('finished');
  });

  res.render('index', { title: 'WIMS' });
});

module.exports = router;
