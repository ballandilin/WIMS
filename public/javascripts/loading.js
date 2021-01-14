$(function() {
    var btn = $("#python");
    var img = $('#imgLoad').attr('src');
    
    // if (img != '' ) { 
        btn.on("click", function() {

            $(this).addClass('btn__progress');
            setTimeout(function() {
                btn.addClass('btn__progress--fill')
            }, 500);
            setTimeout(function() {
                btn.removeClass('btn__progress--fill')
            }, 5100);
            //   setTimeout(function() {
            //     btn.addClass('btn__complete')
            //   }, 4400);
        });
    // }
  })