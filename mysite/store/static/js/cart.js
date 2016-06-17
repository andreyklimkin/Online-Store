$(document).ready(function(){
    cur_loc = location.toString()
    cur_loc = cur_loc.substring(cur_loc.length - 5)
    /*if(cur_loc == "Cart/") {
        make_total();
    } */
    make_total();

    function make_total() {
        var items = $('.item-total')
        var total = 0;
        for (i = 0; i < items.length; ++i) {
            cost = $(items[i]).text().trim().substring(1)
            total += parseFloat(cost);
        }
        total_str = "$" + total.toString()
        $('.total_cost').text(total_str)
    }

    function get_number() {
        res = ""
        var items = $('.item-total')
        for (i = 0; i < items.length; ++i) {
            cost = $(items[i]).text().trim().substring(1)
            id = $(items[i]).attr('tot-id')
            res = res + id + "$"
            res = res + cost + "$"
        }
        return res;
    }

    $( ".add" ).click(function(){
        var current_button = $(this);
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
                        current_button.addClass("disabled")
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
        id = ($(this).attr('rmv_id'))
        $.ajax({
            url: "/delete_from_cart/",
            type: "GET",
            data: {"item": $(this).attr('rmv_id')},
            success: function(data){
                //alert(data)
                //alert(id)
                del_obj = document.getElementById(id)
                //$(del_obj).css('height', 0);
                $(del_obj).hide(500, function() {
                    $(del_obj).remove();
                    make_total();
                });
            }
        });

    });

    $( ".form" ).change(function() {
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
        make_total()
	})

    $( ".paypal_img" ).click(function(){
        price = $('.total_cost').text().trim().substring(1);
        item_price = get_number()
        //alert(item_price)
        alert(item_price)
        $.ajax({
            url: "/payment/cart/",
            type: "GET",
            data: {"total_price": price, "item_price": item_price},
            success: function(data){
                $('body').html(data);
                //alert(data)
            }
        });
    })

    $( "#target" ).submit(function( event ) {
        var text = $('#search').val();
        $.ajax({
            url: "/search",
            type: "GET",
            data: {"str": text},
            success: function(data){
                $('body').html(data);
                //alert(data)
            }
        });
        event.preventDefault();
    });
  });
