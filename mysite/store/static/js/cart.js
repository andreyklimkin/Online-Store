$(document).ready(function(){
    $( "button.add" ).click(function(){
        alert("watches have been added to your cart");
        var current_button = $(this);
        var html = ['<button class=\"btn btn-success btn-md add\"',
                    'id=\"item{{ watch.model }}\">',
                    'Is already in the cart'].join('\n');
        /*$(current_button).replaceWith( html );*/
        //$(this).сss("background-color:grey");
        $.ajax({
            url: "/add-to-cart/",
            type: "GET",
            data: {"item": $(this).attr('id')},
            success: function(data){
            current_button.text( data );
            }
        });
    });
  });