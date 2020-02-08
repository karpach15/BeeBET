jQuery('document').ready(function(){
	if ($(window).width() < 1890){
		var medi_queries = $('.style_notebook').text();
		$('.media_style').html(medi_queries);
		$('.btns').css('display', 'none');
		$('.btns_media').css('display', 'grid');
		$('.btns_media .active img').attr('src', '/static/main/img/helmet_active.png');
		var pop_up = $('.popUp .driver_details').height();
		var pop_up = pop_up - 350 + 'px';
		$('.popUp .info').css('height', pop_up);

		$('.notification .img_border').appendTo('.notification .info');
	}
	if ($(window).width() < 1200){
		var medi_queries = $('.style_phone').text();
		$('.media_style').html(medi_queries);
	}
});