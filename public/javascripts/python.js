$('document').ready(function () {

    var soc = io();

  $('#python').click(function(){
    var img = $('#imgLoad').attr('src');
    var data = { img : img };
    if (img === '' ) {
      alert("Une image est necessaire");
    } else {
      $.ajax({
          type: "POST",
          url: "/pythonData/",
          processData: false,
          contentType: 'application/json',
          data: JSON.stringify(data),
          success: function(r) {
            console.log(r);
          }
      });
    }
    // $.post("/pythonData/",{img:img},function(data){

    //   console.log("done");
    //   document.location.href = "/";
    // });
  });

  soc.on('result', function(result) {
    // $("#result").text(result);
    $("#popup1 h2").first().text(result);

    $('.popup img').first().attr('src',"/compare/img/imgSet/" + result + "/0.jpg");
    // $("#popup").click();
    window.location.href = "#popup1";
  })


});

