$('document').ready(function () {

    $('#python').mouseover(function(){
        this.setAttribute('src', '../images/bouclierSombre2.png');
    });

    $('#python').mouseleave(function(){
        this.setAttribute('src', '../images/bouclier2.png');
    });
});