$( document ).ready( function () {

        $( window ).scroll( function () {
            console.log( this.scrollY );
    
    
            if ( this.scrollY > 100 ) {
                $( '.navbar_box' ).addClass( 'bg-primary' );
                $( '.navbar_box' ).removeClass( 'py-3' );
    
            } else {
                $( '.navbar_box' ).removeClass( 'bg-primary' );
                $( '.navbar_box' ).addClass( 'py-3' );
            }   
        } );
    
    var accTop = $( '.acc-top' );

    accTop.click( function ( e ) {
        e.preventDefault();

        $( this ).next().slideToggle();
        accTop.not( this ).next().slideUp();

        $( this )
            .children( ".fas" )
            .toggleClass( "acc-icon-active" );
        a.not( this )
            .children( ".fas" )
            .removeClass( "acc-icon-active" );

    } );





    var isCarouselPaused = false;

$( window ).on( 'load resize', function() {
  if ( document.documentElement.clientWidth <= 767 ) {
    if ( !isCarouselPaused ) {
      $( '#myCarousel' ).carousel('pause');
      isCarouselPaused = true;
    }
  } else {
    if ( isCarouselPaused ) {
      $( '#myCarousel' ).carousel('cycle');
      isCarouselPaused = false;
    }
  };
});


    

} );