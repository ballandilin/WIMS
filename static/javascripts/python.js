$('document').ready(function () {

  var soc = io();

  $('#python').click(function(){
    var img = $('#imgLoad').attr('src');
    var data = { img : img };
    if (img === '' ) {
      alert("Une image est necessaire");
    } else {

      $("#python").text("waiting...");
      $.ajax({
          type: "POST",
          url: "/",
          processData: false,
          contentType: 'application/json',
          data: JSON.stringify(data),
          success: function(r) {
            console.log(r);
          },
          statusCode: {
            500: function() {
              alert("Une erreur est survenue dans le processus");
              $("#python").text("Retry !");
            },
            404: function() {
              alert("Une erreur est survenue dans le processus");
              $("#python").text("Retry !");
            }
          }
      });
    }

  });

  soc.on('result', function(result) {

    $("#popup1 h2").first().text(result);
    $("#python").text("Find !");
    $('.popup img').first().attr('src',"/static/celeb/" + result + "/0.jpg");
    // $("#popup").click();
    window.location.href = "#popup1";
  })


});

