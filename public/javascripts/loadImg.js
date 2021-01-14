$('document').ready(function () {
  $('#click').click(function(){
    $("#imgupload")[0].click();
  });

  /**
   * Lorsque l'etat du cadre comportant l'image change (ajout d'une image) on recupere le fichier
   */
  $("#imgupload").change(function () {
    
    /**
     * Si il y a un fichier on ouvre une instance de FileReader afin de recuperer le fichier 
     */
    if (this.files && this.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {

        var img = e.target.result;

        $('#imgLoad').attr('src', img);
        }
        // imageToDataUri(img, 300, 300);
        reader.readAsDataURL(this.files[0]);
        }
    });
});

