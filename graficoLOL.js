var flag = true;
function crearLOL () {
    if(flag == true){
        // create a new div element
    var newDiv = document.createElement("div");
    newDiv.className = "image";
    newDiv.style.height = "715px";
    newDiv.style.width = "600px";
    //newDiv.style.backgroundColor = "white";
    newDiv.style.backgroundImage = "url(\"images\/grieta.jpg\")";
    newDiv.style.backgroundRepeat = "no-repeat";
    //newDiv.style.backgroundPosition= "";
    newDiv.style.backgroundSize = "100% auto";
    var cont = document.getElementById("lol");
    cont.appendChild(newDiv);
    //se crea el div top
    var top = document.createElement("div");
    //se agregan Los TOPS
    top.className = "top";
    newDiv.appendChild(top);
        var TopRed = document.createElement("p");
        TopRed.className = "topRed";
        TopRed.innerHTML = "topRed";//AGREGAR VALOR DE LOS DATOS
        TopRed.style.paddingTop = "80px";
        TopRed.style.paddingLeft = "160px";
        TopRed.style.color = "red";
        var TopBlue = document.createElement("p");
        TopBlue.className = "topBlue";
        TopBlue.innerHTML = "topBlue";//AGREGAR VALOR DE LOS DATOS
        TopBlue.style.paddingTop = "5px";
        TopBlue.style.paddingLeft = "100px";
        TopBlue.style.color = "blue";
        top.appendChild(TopRed);
        top.appendChild(TopBlue);
    //se agrega el Jungle Blue
    var jungles = document.createElement("div");
    jungles.className = "jungleBlue";
    newDiv.appendChild(jungles);
        var jungleBlue = document.createElement("p");
        jungleBlue.className = "jungleBlue";
        jungleBlue.innerHTML = "jungleBlue";//AGREGAR VALOR DE LOS DATOS
        jungleBlue.style.paddingTop = "50px";
        jungleBlue.style.paddingLeft = "130px";
        jungleBlue.style.color = "blue";
        jungles.appendChild(jungleBlue);
    //se agregan Los MIDS
    var mids = document.createElement("div");
    mids.className = "mid";
    newDiv.appendChild(mids);
        var midRed = document.createElement("p");
        midRed.className = "midRed";
        midRed.innerHTML = "midRed";//AGREGAR VALOR DE LOS DATOS
        midRed.style.paddingLeft = "310px";
        midRed.style.color = "red";
        var midBlue = document.createElement("p");
        midBlue.className = "midBlue";
        midBlue.innerHTML = "midBlue";//AGREGAR VALOR DE LOS DATOS
        midBlue.style.paddingLeft = "270px";
        midBlue.style.color = "blue";
        var jungleRed = document.createElement("p");
        jungleRed.className = "jungleRed";
        jungleRed.innerHTML = "jungleRed";//AGREGAR VALOR DE LOS DATOS
        jungleRed.style.paddingLeft = "440px";
        jungleRed.style.color = "red";
        mids.appendChild(midRed);
        mids.appendChild(midBlue);
        mids.appendChild(jungleRed);
    //se agregan Los Support y Tiradores
    var SoporteTirador = document.createElement("div");
    SoporteTirador.className = "SoporteTirador";
    newDiv.appendChild(SoporteTirador);
        var supportRed = document.createElement("p");
        supportRed.className = "supportRed";
        supportRed.innerHTML = "supportRed";//AGREGAR VALOR DE LOS DATOS
        supportRed.style.paddingLeft = "490px";
        supportRed.style.color = "red";
        var shooterRed = document.createElement("p");
        shooterRed.className = "tiradorRed";
        shooterRed.innerHTML = "shooterRed";//AGREGAR VALOR DE LOS DATOS
        shooterRed.style.paddingTop = "5px";
        shooterRed.style.paddingLeft = "490px";
        shooterRed.style.color = "red";
        var supportBlue = document.createElement("p");
        supportBlue.className = "supportBlue";
        supportBlue.innerHTML = "supportBlue";//AGREGAR VALOR DE LOS DATOS
        supportBlue.style.paddingLeft = "440px";
        supportBlue.style.color = "blue";
        var shooterBlue = document.createElement("p");
        shooterBlue.className = "tiradorBlue";
        shooterBlue.innerHTML = "shooterBlue";//AGREGAR VALOR DE LOS DATOS
        shooterBlue.style.paddingLeft = "440px";
        shooterBlue.style.color = "blue";

        SoporteTirador.appendChild(supportRed);
        SoporteTirador.appendChild(shooterRed);
        SoporteTirador.appendChild(supportBlue);
        SoporteTirador.appendChild(shooterBlue);
        var link = document.createElement("link");
        link.rel = "stylesheet";
        link.href = "style.css";
        flag = false;
    }
    else{
        flag = true;
        
    }
  }
