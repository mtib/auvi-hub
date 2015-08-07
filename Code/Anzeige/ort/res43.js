var imgholder = document.getElementById("imgholder");

function ratio(obj, w, h){
	height = window.innerHeight;
	width = height/h*w;
	obj.style.height = height+"px";
	obj.style.width = width+"px";
}

function aspect () {
	ratio (imgholder, 4, 3);
}

aspect();