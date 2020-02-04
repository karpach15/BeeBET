jQuery('document').ready(function(){
	if ($(window).width() < 1890){
		var medi_queries = $('.style').text();
		$('.media_style').html(medi_queries);
		$('.btns').css('display', 'none');
		$('.btns_media').css('display', 'grid');
		$('.btns_media .active img').attr('src', '/static/main/img/helmet_active.png');
			var pop_up = $('.popUp .driver_details').height();
			var pop_up = pop_up - 350 + 'px';
			$('.popUp .info').css('height', pop_up);
	}
});