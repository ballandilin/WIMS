var express = require('express');
var router = express.Router();



/* GET python page */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'WIMS'});
});




router.post('/', function(req, res, next) {

  var img = req.body.img;

  py(img, res);

  res.send(req.session)
});


module.exports = router;

/**
 * Function permettant de gerer le fonctionnement du programme python, l'envoie de l'image et la reception des resultat
 * @param {*} img 
 * @param {*} res 
 */
function py(img, res) {

  let {PythonShell} = require('python-shell')

  let options = {
    pythonOptions: ['-u'], // get print results in real-time
    scriptPath: 'public/compare'
};

  // on commence une nouvelle instance de PythonShell
  myscript = new PythonShell('main.py', options);
  myscript.send(img);
  var results = [];

  // on recupere chaque message renvoyé par le programme python via un print
  myscript.on('message', function(message) {
    results.push(message);
  });


  myscript.end(function(err, code, signal) {    
    if (err) {
      console.log(err);
      // si il n'y as aucun resultat on renvoie aucun visage
      results.push("face not found");
    };
    console.log(results);
    res.io.emit("result", results[0]);            
  });

}