// $('#click').click(function(){
//   console.log("click");
//   $('#imgupload').trigger('click');
// });

$('document').ready(function () {
  $('#click').click(function(){
    $("#imgupload")[0].click();
  });
  $("#imgupload").change(function () {
    if (this.files && this.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {
        $('#imgLoad').attr('src', e.target.result);
        }
        reader.readAsDataURL(this.files[0]);
        }
    });
});
