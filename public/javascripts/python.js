$('document').ready(function () {

    var soc = io();

  $('#python').click(function(){
    var img = $('#imgLoad').attr('src');
    $.post("/pythonData/",{img:img},function(data){
      console.log("done");
      document.location.href = "/";
    });
  });

  soc.on('result', function(result) {
    // $("#result").text(result);
    $("#popup1 h2").first().text(result);
    // $("#popup").click();
    window.location.href = "#popup1";
  })


});

