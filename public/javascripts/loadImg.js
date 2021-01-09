$('document').ready(function () {
  $('#click').click(function(){
    $("#imgupload")[0].click();
  });
  $("#imgupload").change(function () {
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

