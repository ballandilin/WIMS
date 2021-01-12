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
            $("#python").text("fonctionne");
          },
          statusCode: {
            500: function() {
              alert("Une erreur est survenue dans le processus");
              $("#python").text("Find !");
            },
            404: function() {
              alert("Une erreur est survenue dans le processus");
              $("#python").text("Find !");
            }
          }
      });
    }

  });

  soc.on('result', function(result) {
    // $("#result").text(result);
    console.log(result);
    $("#popup1 h2").first().text(result);
    $("#python").text("Find !");
    $('.popup img').first().attr('src',"/static/celeb/" + result + "/0.jpg");
    // $("#popup").click();
    window.location.href = "#popup1";
  })


});

