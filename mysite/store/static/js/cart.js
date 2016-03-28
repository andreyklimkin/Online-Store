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

    $("select").click(function() {
    	var n = $(this).val()
    	price_id = $(this).attr('price-id')
    	total_id = $(this).attr('total-id')
    	price_elem = document.getElementById(price_id)
    	total_elem = document.getElementById(total_id)
    	cost = $(price_elem).text().trim().substring(1)
    	var total = parseFloat(cost) * n;
    	total = total.toFixed(2)
    	total_str = "$" + total.toString()
    	$(total_elem).text(total_str)
	})

  });
