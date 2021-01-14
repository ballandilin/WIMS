var express = require('express');
var router = express.Router();


/* GET home page. theme 3 */
router.get('/', function(req, res, next) {
  res.render('index3', { title: 'Who Is My Double'});
});

module.exports = router;
