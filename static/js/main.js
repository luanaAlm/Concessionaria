$(document).ready(function(){
    /* ---owl carousel Destaques--- */
    $('.destaques-carousel').owlCarousel({
        loop:true,
        margin:0,
        autoplay:true,
        responsiveClass:true,
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:2,
            },
            1000:{
                items:3,
            }
        }
    });

    /* ---owl carousel Depoimentos--- */
    $('.depoimentos-carousel').owlCarousel({
        loop:true,
        margin:0,
        autoplay:true,
        responsiveClass:true,
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:2,
            },
            1000:{
                items:3,
            }
        }
    });
    /* --- navbar - collapse --- */
    $(".nav-link").on("click", function(){
        $(".navbar-collapse").collapse("hide");
    });
    
    /* ---magnific-popup --- */
    $('.parent-container').magnificPopup({
        delegate: 'a', // child items selector, by clicking on it popup will open
        type: 'image',
        gallery:{enabled:true}
        // other options
    });
})