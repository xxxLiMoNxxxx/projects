function ControlloImmediato(object){
	 
	
	//Nome
	if(object.id=="nome"){
		var obj = document.getElementById('nome');
		var espress = /^([a-zA-Z\xE0\xE8\xE9\xF9\xF2\xEC\x27]\s?)+$/;
		if(obj.value.length < 1 || !espress.test(obj.value)){
			object.style.border = "1.5px solid red";
			object.style.background = "#ffcccc";
		}
		else {
			object.style.border = "1.5px solid green";
			object.style.background = "#cce5cc";
		}
	}
	//tipo
	
	else if(object.id=="tipo"){
		var obj = document.getElementById('tipo').value;
	 
	  if (obj=='')  	  {
		object.style.border = "1.5px solid red";
		object.style.background = "#ffcccc";
		}
	else {
		object.style.border = "1.5px solid green";
		object.style.background = "#cce5cc";
	}

	}

	//Email
	else if(object.id=="email"){
		var obj = document.getElementById('email');
		var espress = /^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
		if(obj.value.length < 1 || !espress.test(obj.value)){
			object.style.border = "1.5px solid red";
			object.style.background = "#ffcccc";
		}
		else {
			object.style.border = "1.5px solid green";
			object.style.background = "#cce5cc";
		}
	} 
	//Telefono
	else if (object.id=="telefono"){
		var obj = document.getElementById('telefono');
		var espress = /^\+?([0-9\-]\s?)+\*?$/;
		var meno = /\B\-/;
		if(obj.value.length < 1 || !espress.test(obj.value) || meno.test(obj.value)){
			object.style.border = "1.5px solid red";
			object.style.background = "#ffcccc";
		}
		else {
			object.style.border = "1.5px solid green";
			object.style.background = "#cce5cc";
		}
	}
	 
	//Ceckbox
	else if (object.id=="Con_Si"){
		var obj = document.getElementById('Con_Si');
		if(obj.checked){
			document.getElementById('labelaccons').style.color = "green";
		}
		else {

			document.getElementById('labelaccons').style.color = "red";
		}
	}
	else{
		object.style.border = "1px solid";
	}

}

function ControllaForm(object){
	
	 
	var nome = document.getElementById('nome');	
	var cognome = document.getElementById('cognome');
	 
	var email = document.getElementById('email');
	 
	var telefono = document.getElementById('telefono');
	 
 	var privacy = document.getElementById('privacy');
	 
	
	var espressnome = /^([a-zA-Z\xE0\xE8\xE9\xF9\xF2\xEC\x27]\s?)+$/;
	var espressemail = /^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
	var espresstelefono = /^\+?([0-9\-]\s?)+\*?$/;
	var espresscap = /^\d{5}$/;
	
	
 
		 
		 
	return true;
}
