$( function() { // TODO uniquement sur Spécial:Nouvelles_pages
    $( '<a>bienvenuter</a>' ).click( function() {
	var api = new mw.Api();
	api.get(
	    {
		"action": "query",
		"format": "json",
		"meta": "tokens"
	    }
	).done( function ( data ) {
	    api.post(
		{
		    "action": "edit",
		    "format": "json",
		    "title": "User:Arktest/bienvenue", // TODO PdD de l'utilisateur
		    "section": "new",
		    "sectiontitle": "Bienvenue sur Wikipédia !",
		    "text": "Hello !~~~~", // TODO message de bienvenue
		    "summary": "Bienvenue !",
		    "token": data.query.tokens.csrftoken
		}
	    ).done( function ( data ) {
		console.log( 'CEFE!' ); // TODO feedback
	    } );
	} );
    } ).insertAfter( $( '.mw-usertoollinks-contribs' ) ).before( ' | ' );
} );
