$('document').ready(function () {

    var soc = io();

  $('#python').click(function(){

    // on recupere la source de l'image
    var img = $('#imgLoad').attr('src');
    // on formate les données sous forme de dictionnaire
    var data = { img : img };

    // Si l'image est vide alors on le montre a l'utilisateur
    if (img === '' ) {
      alert("Une image est necessaire");
    } else {
      $("#python").text("waiting...");
      // On creer la requete a envoyer au programme python
      $.ajax({
          type: "POST",
          url: "/pythonData/",
          processData: false,
          contentType: 'application/json',
          data: JSON.stringify(data),
          success: function(r) {
            console.log("fonctionne");
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

  // on utilise les websocket pour recuperer le moment ou un resultat est renvoyer
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

