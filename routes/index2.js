var express = require('express');
var router = express.Router();


/* GET home page. theme 2 */
router.get('/', function(req, res, next) {
  res.render('index2', { title: 'Who Is My Double'});
});


module.exports = router;
