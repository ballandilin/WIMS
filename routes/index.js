var express = require('express');
var router = express.Router();


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Who Is My Double', theme: 'theme1.css'});
});

router.get('/:theme', function(req, res, next) {
    var theme = req.params.theme;
  res.render('index', { title: 'Who Is My Double', theme: theme});
});


module.exports = router;
