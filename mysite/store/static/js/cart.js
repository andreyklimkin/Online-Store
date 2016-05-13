$(document).ready(function(){
    $( "button.add" ).click(function(){
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
                //alert(data)
                if(data=="NR") {
                    alert("You are not registred. Log in and try again");
                } else {
                	if(data=="IsIn") {
                		alert("wathces is already in your cart");
                	} else {
                    	current_button.addClass("disabled")
                    	current_button.text( data );
                    	alert("watches have been added to your cart");
                    }
                }
            }
        });
    });

    $( ".rmv" ).click(function(){
        var current_button = $(this);
        $.ajax({
            url: "/delete_from_cart/",
            type: "GET",
            data: {"item": $(this).attr('rmv_id')},
            success: function(data){
                //alert(data)

                location.reload()
            }
        });

    });

    $( ".form-control" ).change(function() {
    	var str = $(this).val()
    	pos = str.search(":")
    	brand=str.substring(0, pos - 1)
    	col =str.substring(pos + 2)
  		$.ajax({
            url: "/order_collections/",
            type: "GET",
            data: {"brand": brand, "collection": col},
            success: function(data){
            	$('body').html(data);
            }
        });
	});

    $("select").change(function() {
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
