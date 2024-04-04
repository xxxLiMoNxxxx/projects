
function attiva_uno(){
		pulsante_uno.style.background ="white";
		pulsante_due.style.background =" #223741";
		pulsante_tre.style.background =" #223741";
		cont_terza_uno.style.display = "flex";
		cont_terza_due.style.display = "none";
		cont_terza_tre.style.display = "none";
	}
	function attiva_due(){
		pulsante_uno.style.background ="#223741";
		pulsante_due.style.background ="white";
		pulsante_tre.style.background ="#223741";
		cont_terza_uno.style.display = "none";
		cont_terza_due.style.display = "flex";
		cont_terza_tre.style.display = "none";
	
	}
	function attiva_tre(){
		pulsante_uno.style.background ="#223741";
		pulsante_due.style.background ="#223741";
		pulsante_tre.style.background ="white";
		cont_terza_uno.style.display = "none";
		cont_terza_due.style.display = "none";
		cont_terza_tre.style.display = "flex";
	}
	function avanti1(){
			form1.style.display = "none";
			form2.style.display = "block";
	}
	function avanti2(){
			
		
			if(nome.value == ''){
				alert('Nome Mancante');
			}else if(cognome.value == ''){
				alert('Cognome Mancante');
			}else if(email.value == ''){
				alert('Email Mancante');
			}else if(telefono.value == ''){ 
				alert('Telefono Mancante');
			}else if( 	document.getElementById('telefono').style.border != "1.5px solid green"){
				alert('Inserire un numero di telefono corretto');
			}else{
				form2.style.display = "none";
				form3.style.display = "block";		
			}
		
	}
	function indietro2(){
			form1.style.display = "block";
			form2.style.display = "none";
	}
	function indietro3(){
			form2.style.display = "block";
			form3.style.display = "none";
	}
	
	function attiva_uno_mob(){
		
		pulsante_uno_mob.style.background ="white";
		pulsante_due_mob.style.background ="#223741";
		pulsante_tre_mob.style.background ="#223741";
	
		uno_mob.style.display = "inline-block";
		due_mob.style.display = "none";
		tre_mob.style.display = "none";
		
	}
	function attiva_due_mob(){
		pulsante_uno_mob.style.background ="#223741";
		pulsante_due_mob.style.background ="white";
		pulsante_tre_mob.style.background ="#223741";
	
		uno_mob.style.display = "none";
		due_mob.style.display = "inline-block";
		tre_mob.style.display = "none";
	
	}
	function attiva_tre_mob(){
		pulsante_uno_mob.style.background ="#223741";
		pulsante_due_mob.style.background ="#223741";
		pulsante_tre_mob.style.background ="white";

		uno_mob.style.display = "none";
		due_mob.style.display = "none";
		tre_mob.style.display = "inline-block";
	
	}
	function attiva_quattro_mob(){
		pulsante_uno_mob.style.background ="grey";
		pulsante_due_mob.style.background ="grey";
		pulsante_tre_mob.style.background ="grey";
	
		uno_mob.style.display = "none";
		due_mob.style.display = "none";
		tre_mob.style.display = "none";
	
	}
	function attiva_cinque_mob(){
		pulsante_uno_mob.style.background ="grey";
		pulsante_due_mob.style.background ="grey";
		pulsante_tre_mob.style.background ="grey";
		
		uno_mob.style.display = "none";
		due_mob.style.display = "none";
		tre_mob.style.display = "none";
		
	}
	 function avvia_cellulareee() 
	{

		
		telefono = document.getElementById('telefono');		
		telefonov = document.getElementById('telefono').value;		
//	    alert(telefono);
		telefonol = document.getElementById('telefono').length;		 
			alert(telefono);
			alert(telefonov);
			alert(telefonol);

		if((telefonol = 9) || (telefonol = 10) )
		{ 
			alert('OOK');			
			document.getElementById('telefono').style.border = "1.5px solid green";
			document.getElementById('telefono').style.background = "rgb(204, 229, 204)";
		
		
		}else {
			document.getElementById('telefono').style.border = "2px solid red";
			alert ('Inserire un numero di telefono corretto');
		};
		
	}		
		

	function avvia_cellulare()
	{
		telefono = document.getElementById('telefono').value;
		//		alert(telefono.length);
		if (  (  (telefono.length == 9 ) ||  (telefono.length == 10 )) && ((telefono.substr(0,1))==3)  ) {
			document.getElementById('telefono').style.border = "1.5px solid green";
			document.getElementById('telefono').style.background = "rgb(204, 229, 204)";
			document.getElementById("submit").disabled = false;
			return true;	
		}
		
		else {
			document.getElementById('telefono').style.border = "2px solid red";
			alert('Inserire un numero di telefono corretto');
			document.getElementById("submit").disabled = true;
			
						return false;
		}
	}















		function avvia_cellulares(ele) 
		{    
			
				  cellulare = (document.getElementById('cellulare').value);
				// alert('controlla');
			 
				//alert(telefono);
				 /*351", "352", "330", "331", "333", "334", "335", "336", "337", "338", "339", "360", "366", "368", "340", "342", 
				 "344", "345", "346", "347", "348", "349", "320", "324", "327", "328", "329", "380", "388", "389", "391", "392",
				  "393", "377", "379", "371", "370", "353", "373", "375", "350", "378", "376"];*/
			 
			 if(ele.id=="cellulare"){
						// Controlli formali sul numeo
				if((telefono.length < 9) || (ele.value.length > 10) ||(ele.value == '')  || (!scan1(ele.value )) ||
				(  
				(!ele.value.startsWith("35"))  //Iliad Italia: 351-3, 351-4, 351-5, 351-6, 351-7, 351-8, 351-9, 352-0
				&& (!ele.value.startsWith("33"))  //TIM: 330, 331, 333, 334, 335, 336, 337, 338, 339, 360, 361*, 362*, 363*, 366, 368, 381*
				&& (!ele.value.startsWith("360"))
				&& (!ele.value.startsWith("366"))
				&& (!ele.value.startsWith("368"))
				&& (!ele.value.startsWith("340"))  //Vodafone Italia: 340, 341*, 342, 343*, 344, 345, 346, 347, 348, 349, 383*
				&& (!ele.value.startsWith("342"))
				&& (!ele.value.startsWith("344"))
				&& (!ele.value.startsWith("345"))
				&& (!ele.value.startsWith("346"))
				&& (!ele.value.startsWith("347"))
				&& (!ele.value.startsWith("348")) 
				&& (!ele.value.startsWith("349"))
				&& (!ele.value.startsWith("320"))   //Wind: 320, 322*, 323*, 324, 327, 328, 329, 355*, 380, 388, 389 
				&& (!ele.value.startsWith("324")) 			 
				&& (!ele.value.startsWith("327")) 
				&& (!ele.value.startsWith("328")) 
				&& (!ele.value.startsWith("329")) 
				&& (!ele.value.startsWith("380")) 
				&& (!ele.value.startsWith("388")) 
				&& (!ele.value.startsWith("389")) 
				&& (!ele.value.startsWith("391")) //Tre: 390*, 391, 392, 393, 397*
				&& (!ele.value.startsWith("392")) 
				&& (!ele.value.startsWith("393"))  
				&& (!ele.value.startsWith("377"))  
				&& (!ele.value.startsWith("378"))  
				&& (!ele.value.startsWith("350"))  
				&& (!ele.value.startsWith("375"))  
				&& (!ele.value.startsWith("373"))  
				&& (!ele.value.startsWith("388"))  
				&& (!ele.value.startsWith("389"))  
				&& (!ele.value.startsWith("391"))  
				&& (!ele.value.startsWith("392"))  
				&& (!ele.value.startsWith("377"))  
				&& (!ele.value.startsWith("379"))  
				&& (!ele.value.startsWith("371"))  
				&& (!ele.value.startsWith("353"))  
				&& (!ele.value.startsWith("370"))  
				&& (!ele.value.startsWith("370"))  
				&& (!ele.value.startsWith("370"))  
				&& (!ele.value.startsWith("352"))  
				&& (!ele.value.startsWith("351"))  
				&& (!ele.value.startsWith("331"))  
				&& (!ele.value.startsWith("333"))  
				&& (!ele.value.startsWith("334"))  
				&& (!ele.value.startsWith("335"))  
				&& (!ele.value.startsWith("336"))  
				&& (!ele.value.startsWith("337"))  
				&& (!ele.value.startsWith("329"))  
				&& (!ele.value.startsWith("380"))  
				)
				){ 
					alert('controllo KO');
				ele.style.border = "2px solid red";
				document.getElementById('excla_telefono').style.display='block';
				document.getElementById('kocell').style.display='block';
				$("#kocell").show(); 
				
				$("#attesa").hide();
				$("#okcell").hide(); 
			
			 
							//alert(ele.value);
				 /*351", "352", "330", "331", "333", "334", "335", "336", "337", "338", "339", "360", "366", "368", "340", "342", 
				 "344", "345", "346", "347", "348", "349", "320", "324", "327", "328", "329", "380", "388", "389", "391", "392",
				  "393", "377", "379", "371", "370", "353", "373", "375", "350", "378", "376"];*/
			}
			 
								else 
									 {  
										alert('controllo OK');
												$("#attesa").hide();
												 $("#okcell").show(); 
												$("#kocell").hide();  
												ele.style.border = '1px solid gray';
												$("#excla_telefono").hide(); 
												document.getElementById('submit').style.disabled= false;
											 
									 
									}
							 
			 }
				   
			 
		}
						
			   
		 
	
	