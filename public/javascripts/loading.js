$(function() {
    var btn = $("#python");

    /**
     * Au click du bouton une barre de progression apparait
     */
    btn.on("click", function() {

        $(this).addClass('btn__progress');
        setTimeout(function() {
            btn.addClass('btn__progress--fill')
        }, 500);
        setTimeout(function() {
            btn.removeClass('btn__progress--fill')
        }, 7000);

    });
  })