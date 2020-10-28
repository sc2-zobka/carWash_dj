let url = "https://api.control-z.cl/api/feriados"


fetch(url)
    .then(function(respuesta) {
        return respuesta.json()
    })
    .then(function(respuesta) {
        let fecha_loc = new Date()
        let fecha_str = " "
        let fecha_nom
        //let fecha_fes
        
        respuesta.forEach(function(info) {
            let fecha_tmp = new Date(info.fecha.split("-").join("/"))
            if (fecha_tmp > fecha_loc) {
                if ( fecha_str == " " ) {
                    fecha_str = fecha_tmp
                    fecha_nom = info.nombre
                    //fecha_fes = info.fecha
                }
                return
            }
        })

        let enlaceFeriado = document.getElementById("feriado")
        //enlaceFeriado.innerText = respuesta[0].fecha
        enlaceFeriado.innerText = fecha_nom

    })