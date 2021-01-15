$('document').ready(function () {

    // Si la souris passe sur le bouclier on change l'image
    $('#python').mouseover(function(){
        this.setAttribute('src', '../static/bouclierSombre2.png');
    });

    // Si la souris sors du rayon d'action du bouclier alors ont remet l'ancienne image
    $('#python').mouseleave(function(){
        this.setAttribute('src', '../static/bouclier2.png');
    });
});