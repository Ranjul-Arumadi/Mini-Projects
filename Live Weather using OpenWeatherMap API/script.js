var city1="Kannur,IN";
var city2="Manama, BH";
var city3="Bengaluru, IN";
var VJEC="lat={12.098101602529287}&lon={75.56040986747851}"; //12.098101602529287, 75.56040986747851
//$.getJSON("https://api.openweathermap.org/data/2.5/weather?q="+city3+"&APPID=42f9e16e518fc14e484ca2dad041ce2e&"

$.getJSON("https://api.openweathermap.org/data/2.5/weather?q="+city1+"&APPID=42f9e16e518fc14e484ca2dad041ce2e&",
function(data)
{
	console.log(data);
	
	var icon= "https://openweathermap.org/img/w/"+ data.weather[0].icon + ".png";
	var temp= Math.floor((data.main.temp)/10)+"°C";
	var weather=data.weather[0].main;
	
	
	var GMTvalue=(5*3600+30*60); //5:30 hours for India
	//SUNRISE
	var unixTimestampSunUp = data.sys.sunrise+GMTvalue; 
    // convert to milliseconds and then create a new Date object
    dateObj1 = new Date(unixTimestampSunUp * 1000); 
    utcString1 = dateObj1.toUTCString(); 
    time1 = utcString1.slice(-11, -7);
	
	//SUNSET
	var unixTimestampSunDown = data.sys.sunset+GMTvalue-(2*3600); 
    // convert to milliseconds and then create a new Date object
    dateObj2 = new Date(unixTimestampSunDown*1000); 
    utcString2 = dateObj2.toUTCString(); 
    time2 = utcString2.slice(-11, -7);
	
	var sunRise="Sun Rise : " +time1+" am";
	var sunSet="Sun Set : " +time2+" pm";

	//console.log(icon);
	
	$('.icon').attr('src',icon);
	$('.weather').append(weather);
	$('.temp').append(temp);
	$('.sunRise').append(sunRise);
	$('.sunSet').append(sunSet);

});