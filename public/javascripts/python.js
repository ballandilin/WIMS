$('document').ready(function () {

    var soc = io();

  // $('#python').mouseover(function(){
  //   this.setAttribute('src', '../images/bouclierSombre2.png');
  // });

  // $('#python').mouseleave(function(){
  //   this.setAttribute('src', '../images/bouclier2.png');
  // });

  $('#python').click(function(){
    var img = $('#imgLoad').attr('src');
    var data = { img : img };
    if (img === '' ) {
      alert("Une image est necessaire");
    } else {
      $("#python").text("waiting...");
      $.ajax({
          type: "POST",
          url: "/pythonData/",
          processData: false,
          contentType: 'application/json',
          data: JSON.stringify(data),
          success: function(r) {
            console.log(r);
          },
          statusCode: {
            500: function() {
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
    $('.popup img').first().attr('src',"../images/celeb/" + result + "/0.jpg");
    // $("#popup").click();
    window.location.href = "#popup1";
  })


});

