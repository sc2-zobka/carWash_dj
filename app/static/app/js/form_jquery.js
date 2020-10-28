/*****************FORMULARIO INSUMOS*****************/

$("#form_i").validate({
    rules:{
      nombre_i:{
        required: true,
        minlength: 3,
        maxlength: 120
      },
      precio_i:{
        required: true,
        number: true,
        min:1
      },
      descripcion_i:{
        minlength: 3,
        maxlength: 200
      }
    }, 
    messages: {
      nombre_i: {
        required: "Este campo es requerido",
        minlength: "minimo debe tener 3 caracteres",
        maxlength: "maximo debe tener 120 caracteres"
      },
      precio_i:{
        required: "Este campo es requerido",
        number: "Debe ser numerico",
        min: "Debe ser mayor a 1"
      },
      descripcion_i:{
        minlength: "minimo debe tener 3 caracteres",
        maxlength: "maximo debe tener 200 caracteres"
      }
    }
})

$("#guardar_i").click(function () {
 
  let nombre_i = $("#nombre_i").val()
  let precio_i = $("#precio_i").val()
  let descripcion_i = $("#descripcion_i").val()
  
})


/******************** FORMULARIO REGISTRAR ***********************/
$("#registrar").click(function () {
 
	let nombre_r = $("#nombre_r").val()
	let rut_r = $("#rut_r").val()
	let apellido_r = $("#apellido_r").val()
	let email_r = $("#email_r").val()
	let fecha_r = $("#fecha_r").val()
	let username_r = $("#username_r").val()
  	let pass_r = $("#pass_r").val()

})
/***************** VALIDATOR PARA FECHA DE NACIMIENTO ***************************/
$.validator.addMethod("fnac", function(value, element, parametro) {
    //value-> lo que escribio el usuario en la caja
    //element -> el elemento html
    //parametro -> lo que se le entrega para validar -> duoc.cl

	//darle formato a la fecha "value"
	//1. value = yyyy-mm-dd  se formatea a -> new Date(yyyy/mm/dd)
	//2. realizar comparacion de fechas


	let formattedDate = new Date(value.split("-").join("/"))
	// data type Date -> yyyy/mm/dd
	
	//console.log(formattedDate + "Fecha procesada")
    if(formattedDate < parametro) {
		console.log("fecha correcta")
		return true;
    }
	console.log("fecha incorrecta");
    return false;
//{0} siempre pasa el parametro recibido por la funcion
}, "Fecha de nacimiento debe ser menos a la actual")

/************************* FUNCION PARA VALIDAR RUT ***************************/
function checkRut(rut) {
	
	// Despejar Puntos
    //let valor = element.val().replace('.','');
	let valor = rut.split(".").join("")
	
	// Despejar Guión
    //valor = valor.replace('-','');
	valor = valor.split("-").join("") 
	
    // Aislar Cuerpo y Dígito Verificador
    cuerpo = valor.slice(0,-1);
    dv = valor.slice(-1).toUpperCase();
    
    // Formatear RUN
    //rut = cuerpo + '-'+ dv
    
	// Si no cumple con el mínimo ej. (n.nnn.nnn)
	//remplazar element.set....   -> rut_r que viene de name="rut_r"
	if(cuerpo.length < 7) {return false;}
	 
	//element.setCustomValidity("RUT Incompleto");
			
    
    // Calcular Dígito Verificador
    suma = 0;
    multiplo = 2;
    
    // Para cada dígito del Cuerpo
    for(i=1;i<=cuerpo.length;i++) {
    
        // Obtener su Producto con el Múltiplo Correspondiente
        index = multiplo * valor.charAt(cuerpo.length - i);
	
        // Sumar al Contador General
        suma = suma + index;
         
        // Consolidar Múltiplo dentro del rango [2,7]
        if(multiplo < 7) { multiplo = multiplo + 1; } else { multiplo = 2; }
  
    }
	
    // Calcular Dígito Verificador en base al Módulo 11
    dvEsperado = 11 - (suma % 11); 
	
    // Casos Especiales (0 y K)
    dv = (dv == 'K')?10:dv;
    dv = (dv == 0)?11:dv;
	
    // Validar que el Cuerpo coincide con su Dígito Verificador
	if(dvEsperado != dv) {return false; }

	return true
}

/************************* VALIDATOR PARA RUT ***************************/
$.validator.addMethod("rutValido", (value, element, parametro) => {

	return checkRut(value, element)

})

$("#form_r").validate({
	rules: {
		rut_r: {
			required: true,
			rutValido: true			
		},
		nombre_r: {
			required: true,
			minlength: 3,
			maxlength: 80
		},
		apellido_r: {
			required: true,
			minlength: 3,
			maxlength: 80
		},
		email_r: {
			required: true,
        	email: true
		},
		fecha_r: {
			required: true,
			fnac : new Date(),
		},
		username_r: {
			required: true,
			minlength: 8
		},
		pass_r: {
			required: true,
			minlength: 8
		}
	},
	//
	messages:{
		rut_r: {
			required: "Este campo es requerido",
			rutValido: "RUT invalido"
			},
			nombre_r:{
				required: "Este campo es requerido",
				minlength: "minimo debe tener 3 caracteres",
				maxlength: "maximo debe tener 80 caracteres"
			},
		apellido_r:{
			required: "Este campo es requerido",
			minlength: "minimo debe tener 3 caracteres",
			maxlength: "maximo debe tener 80 caracteres"
		},
		email_r:{
			required: "Este campo es requerido",
			email: "Email invalido",
		},
		fecha_r:{
			required: "Este campo es requerido"
		},
		username_r:{
			required: "Este campo es requerido",
			minlength: "minimo debe tener 8 caracteres",
		},
		pass_r:{
			required: "Este campo es requerido",
			minlength: "minimo debe tener 8 caracteres",
		}
		
	}
})
