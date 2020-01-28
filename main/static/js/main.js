jQuery('document').ready(function(){
	var account_pic_url = $('.account_pic_url').text();
	$('.profile').css("background", "url(" + account_pic_url + ") no-repeat center top / cover");

	$('.driver:not(#driver_reg)').click(function(){
		$('.popUp').css('display', 'block');
		var driverName = $(this).find('#name').text();
		var driverSurname = $(this).find('#surname').text();
		var racesParticipated = $(this).find('#races_participated').text();
		var racesWon = $(this).find('#races_won').text();
		var regDate = $(this).find('#reg_date').text();
    	var about = $(this).find('#about').text();
    	var profilePic = $(this).find('#profilePic').css('background');
		
		var yearOfGDL = parseInt($(this).find('#year_of_getting_driving_licens').text());
		var monthOfGDL = (parseInt($(this).find('#month_of_getting_driving_licens').text())) - 1;
		var dayOfGDL = parseInt($(this).find('#day_of_getting_driving_licens').text());
		var dateOfGDL = (yearOfGDL + ', ' + monthOfGDL + ', ' + dayOfGDL);
		
		dateOfGDL = new Date(dateOfGDL);
		var today = new Date();
		
		var drivingExpMonths = Math.floor((today - dateOfGDL) / (30.5 * 24 * 60 * 60 * 1000));
		var drivingExpYears = Math.floor((today - dateOfGDL) / (365.25 * 24 * 60 * 60 * 1000));
		
		var years, months;

		if (drivingExpYears == 1){
			years = " год и ";
		}else{
			years = " лет и ";
		}

		if (drivingExpMonths == 1){
			months = " месяц";
		}else if (drivingExpMonths == 2 || drivingExpMonths == 3 || drivingExpMonths == 4){
			months = " месяца";
		}else{
			months = " месяцев";
		}

		if (drivingExpYears == 0){
			if (drivingExpMonths == 0){
				var drivingExp = "Меньше месяца";
			}else{
				var drivingExp = drivingExpMonths + months;
			}
		}else{
			var drivingExp = drivingExpYears + years + drivingExpMonths + months;
		}

    $('.driver_details #name').html(driverName);
    $('.driver_details #surname').html(driverSurname);
    $('.driver_details #races_participated span').html(racesParticipated);
    $('.driver_details #races_won span').html(racesWon);
    $('.driver_details #driving_exp span').html(drivingExp);
    $('.driver_details #reg_date span').html(regDate);
    $('.driver_details .about p').html(about);
    $('.driver_details .img').css('background', profilePic)
	});

	$('.edit').click(function(){
		$('.popUp').css('display', 'block');
	});
	
	$('.close').click(function(){
		$('.popUp').css('display', 'none');
	});


	$('.drivers_list_btn').click(function(){
		$('.popUp').css('display', 'block');
		var drivers = $(this).find('#driver_list').text();
		
		var names = drivers.split("|");
		var drivers = [];
		for (i in names){
			if (i != 0 && i != (names.length - 1)){
				drivers.push(names[i]);
			}
		}
		var drivers_list = []
		for (i in drivers){
			drivers_list.push('<h3 class="driver">' + (parseInt(i) + 1) + '. ' + drivers[i] + '</h3>')
		}
		$('.popUp .drivers_list').html(drivers_list);
	});

	$('.bet_confirm .driver').click(function(){
		$('.choosed').removeClass('choosed');
		$(this).addClass('choosed');
		
		var login = $('.choosed #driver_login').text();
		$('.bet_confirm form .driver_login').attr("value",login);
		$('.bet_confirm form .content .driver_login').html(login);
		
		var race_name = $('#race_name').text();
		$('.bet_confirm form .race_name').attr("value",race_name);

		var coeficient = $(this).find('.info .coeficient').text();
		$('.bet_confirm form .coeficient').attr("value",coeficient);
	});

	$('.reg_result .submit').click(function(){
		$('.accept_bet').submit();
	});

	$('.race').ready(function(){
		time = $('#time_before_race').text();

		hours = time.substr(time.length - 8, time.length - 6);
		hours = parseInt(hours);

		minutes = time.substr(time.length - 5, time.length - 3);
		minutes = parseInt(minutes);

		seconds = time.substr(time.length - 2);
		seconds = parseInt(seconds);

		if ( parseInt(time.substr(time.length - 8, time.length - 8) ) < 10){
			time = time.substr(0, time.length - 7);
		}else{
			time = time.substr(0, time.length - 8);
		}

		setInterval(function(){
			if(minutes == 0 && seconds <= 0){
				seconds = 59;
				minutes = 59;
				hours--;
			}else{
				if(seconds >= 0){
					seconds--;
				}if(seconds < 0){
					seconds = 59;
					minutes--;
				}
			}
			$('#time_before_race').html(time + hours + ':' + minutes + ':' + seconds)
		}, 1000);
	});
});
