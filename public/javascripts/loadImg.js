$('document').ready(function () {
  $('#click').click(function(){
    $("#imgupload")[0].click();
  });
  $("#imgupload").change(function () {
    if (this.files && this.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {

        var img = e.target.result;

        // var prefix = e.target.result.slice(0, 23);
        // var img = e.target.result.slice(24, 0);
        // var compressed = LZString.compress(img);
        // string = LZString.decompress(compressed);


        // my_lzma = new LZMA("../javascripts/lzma_worker.js");
        // my_lzma.compress(img, 9, function on_compress_complete(result) {
        //     console.log("Compressed: " + result);
        //     $('.popup img').first().attr('src', prefix + result);
        //     $('#imgLoad').attr('src', prefix + result);
        // }, function on_compress_progress_update(percent) {
        //     console.log("Compressing: " + (percent * 100) + "%");
        // });


        $('#imgLoad').attr('src', img);
        }
        // imageToDataUri(img, 300, 300);
        reader.readAsDataURL(this.files[0]);
        }
    });
});



function imageToDataUri(img, width, height) {

    // create an off-screen canvas
    var canvas = document.createElement('canvas'),
        ctx = canvas.getContext('2d');

    // set its dimension to target size
    canvas.width = width;
    canvas.height = height;

    // draw source image into the off-screen canvas:
    ctx.drawImage(img, 0, 0, width, height);

    // encode image to data-uri with base64 version of compressed image
    return canvas.toDataURL('image/jpeg', 1);  // quality = [0.0, 1.0]

}



function resizedataURL(datas, wantedWidth, wantedHeight, element)
    {
        // We create an image to receive the Data URI
        // var img = document.createElement('img');

        // When the event "onload" is triggered we can resize the image.
        element.onload = function()
            {        
                // We create a canvas and get its context.
                var canvas = document.createElement('canvas');
                var ctx = canvas.getContext('2d');

                // We set the dimensions at the wanted size.
                canvas.width = wantedWidth;
                canvas.height = wantedHeight;

                // We resize the image with the canvas method drawImage();
                ctx.drawImage(this, 0, 0, wantedWidth, wantedHeight);

                datas = dataURI;

                console.log(canvas.toDataURL());

                return canvas.toDataURL('image/jpeg', 1);


                // var dataURI = canvas.toDataURL();

                // // datas = dataURI;

                // this.src = dataURI;



                /////////////////////////////////////////
                // Use and treat your Data URI here !! //
                /////////////////////////////////////////
            };

        // We put the Data URI in the image's src attribute
        // element.src = datas;
    }