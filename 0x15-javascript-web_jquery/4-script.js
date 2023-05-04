$('DIV#toggle_header').click(function(){
//	$('header').toggleClass('green');
	if($('header').hasClass('green')){
		$('header').removeClass('green');
		$('header').addClass('red');
	}
	else
		$('header').addClass('green');
});
