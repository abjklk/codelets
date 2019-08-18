
function closeMe(){
	document.getElementById('atPopup').style.display="none";
	document.getElementById('blackOverlay').style.display="none";
}

function popUp(date){

	var due = date;
	var split = due.split('|||');
	
	document.getElementById('due').innerHTML = split[0];
	document.getElementById('due2').innerHTML = split[1];

	document.getElementById('atPopup').style.display="block";
	document.getElementById('blackOverlay').style.display="block";
}

function check()
{
/*var dd = document.getElementById('dd').value;
var mm = document.getElementById('mm').value;
var yyyy = document.getElementById('yyyy').value;
var dobs = yyyy+'-'+mm+'-'+dd;*/

var currentdate = document.getElementById('password').value;
var randsting = '';
for(i=0;i<currentdate.length;i++)
{
randsting += currentdate.charAt(i)+randomstring(2);
}

var encodedString = btoa(randsting);
//alert(randsting+" "+encodedString);
document.getElementById('passwd').value = encodedString;
document.getElementById('password').value = encodedString;
return true;
}

function randomstring(L){
    var s= '';
    var randomchar=function(){
    	var n= Math.floor(Math.random()*62);
    	if(n<10) return n; //1-10
    	if(n<36) return String.fromCharCode(n+55); //A-Z
    	return String.fromCharCode(n+61); //a-z
    }
    while(s.length< L) s+= randomchar();
    return s;
}



