var flag = true;
function crearLOL () {
    if(flag == true){
        // create a new div element
        var parms = document.getElementById("opcionesLol");
        parms.appendChild(document.createElement("br")); //mete br

        var labelBlue = document.createElement("p"); 
        labelBlue.id = "labelBlue";
        labelBlue.className = "champName";
        labelBlue.style.color = "#13a5de";
        labelBlue.innerHTML = "Blue Team: ";

        var selector2 = document.createElement("select");
        selector2.id = "select2";
        selector2.style.width = "170px";
        selector2.style.fontFamily = "BeaufortforLOL-Bold";

        var labelRed = document.createElement("p");
        labelRed.id = "labelRed";
        labelRed.className = "champName";
        labelRed.style.color = "#e42d29";
        labelRed.innerHTML = "Red Team: ";
        
        var selector1 = document.createElement("select");
        selector1.id = "select1";
        selector1.style.width = "170px";
        selector1.style.fontFamily = "BeaufortforLOL-Bold";

        var button = document.createElement("button");
        button.id = "btnLoadChamps";
        button.className = "button";
        button.style.width = "150px";
        button.innerHTML = "Cargar Champs";
        button.onclick = loadChamps;
        parms.appendChild(labelBlue);
        parms.appendChild(selector1);
        parms.appendChild(document.createElement("br"));
        parms.appendChild(labelRed);
        parms.appendChild(selector2);
        parms.appendChild(document.createElement("br"));
        parms.appendChild(document.createElement("br"));
        parms.appendChild(button);

        //si hace falta agnadir mas detalles al style
        d3.csv("./Data/blueteams.csv",function(data){
            for(index in data){
                var option = document.createElement("option");
                option.appendChild(document.createTextNode(data[index]["blueteam"]));
                option.value = data[index]["blueteam"];
                selector1.appendChild(option);
            }
        });
        d3.csv("./Data/redteams.csv",function(data){
            for(index in data){
                var option = document.createElement("option");
                option.appendChild(document.createTextNode(data[index]["redteam"]));
                option.value = data[index]["redteam"];
                selector2.appendChild(option);
            }
        });
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
        TopRed.innerHTML = "topRed";//AGREGAR VALOR DE LOS DATOS
        TopRed.className = "champName";
        TopRed.style.paddingTop = "80px";
        TopRed.style.paddingLeft = "160px";
        TopRed.style.color = "#e42d29";
        var TopBlue = document.createElement("p");
        TopBlue.innerHTML = "topBlue";//AGREGAR VALOR DE LOS DATOS
        TopBlue.className = "champName";
        TopBlue.style.paddingTop = "5px";
        TopBlue.style.paddingLeft = "100px";
        TopBlue.style.color = "#13a5de";
        top.appendChild(TopRed);
        top.appendChild(TopBlue);
    //se agrega el Jungle Blue
    var jungles = document.createElement("div");
    jungles.className = "jungleBlue";
    newDiv.appendChild(jungles);
        var jungleBlue = document.createElement("p");
        jungleBlue.innerHTML = "jungleBlue";//AGREGAR VALOR DE LOS DATOS
        jungleBlue.className = "champName";
        jungleBlue.style.paddingTop = "50px";
        jungleBlue.style.paddingLeft = "130px";
        jungleBlue.style.color = "#13a5de";
        jungles.appendChild(jungleBlue);
    //se agregan Los MIDS
    var mids = document.createElement("div");
    mids.className = "mid";
    newDiv.appendChild(mids);
        var midRed = document.createElement("p");
        midRed.className = "champName";
        midRed.innerHTML = "midRed";//AGREGAR VALOR DE LOS DATOS
        midRed.style.paddingLeft = "310px";
        midRed.style.color = "#e42d29";
        var midBlue = document.createElement("p");
        midBlue.className = "champName";
        midBlue.innerHTML = "midBlue";//AGREGAR VALOR DE LOS DATOS
        midBlue.style.paddingLeft = "270px";
        midBlue.style.color = "#13a5de";
        var jungleRed = document.createElement("p");
        jungleRed.className = "champName";
        jungleRed.innerHTML = "jungleRed";//AGREGAR VALOR DE LOS DATOS
        jungleRed.style.paddingLeft = "440px";
        jungleRed.style.color = "#e42d29";
        mids.appendChild(midRed);
        mids.appendChild(midBlue);
        mids.appendChild(jungleRed);
    //se agregan Los Support y Tiradores
    var SoporteTirador = document.createElement("div");
    SoporteTirador.className = "SoporteTirador";
    newDiv.appendChild(SoporteTirador);
        var supportRed = document.createElement("p");
        supportRed.className = "champName";
        supportRed.innerHTML = "supportRed";//AGREGAR VALOR DE LOS DATOS
        supportRed.style.paddingLeft = "490px";
        supportRed.style.color = "#e42d29";
        var shooterRed = document.createElement("p");
        shooterRed.className = "champName";
        shooterRed.innerHTML = "shooterRed";//AGREGAR VALOR DE LOS DATOS
        shooterRed.style.paddingTop = "5px";
        shooterRed.style.paddingLeft = "490px";
        shooterRed.style.color = "#e42d29";
        var supportBlue = document.createElement("p");
        supportBlue.className = "champName";
        supportBlue.innerHTML = "supportBlue";//AGREGAR VALOR DE LOS DATOS
        supportBlue.style.paddingLeft = "440px";
        supportBlue.style.color = "#13a5de";
        var shooterBlue = document.createElement("p");
        shooterBlue.className = "champName";
        shooterBlue.innerHTML = "shooterBlue";//AGREGAR VALOR DE LOS DATOS
        shooterBlue.style.paddingLeft = "440px";
        shooterBlue.style.color = "#13a5de";

        SoporteTirador.appendChild(supportRed);
        SoporteTirador.appendChild(shooterRed);
        SoporteTirador.appendChild(supportBlue);
        SoporteTirador.appendChild(shooterBlue);
        var link = document.createElement("link");
        link.rel = "stylesheet";
        link.href = "style.css";
        flag = false;
        function loadChamps(){
            var redTeam = document.getElementById("select2").value;
            var blueTeam = document.getElementById("select1").value;
            d3.csv("./Data/ChampsPlayedByBlueTeams.csv", function(data){
                for(index in data){
                    var team = data[index]["Team"];
                    console.log(team, " == " , blueTeam);
                    if(team == blueTeam){
                        TopBlue.innerHTML = data[index]["Top"];//AGREGAR VALOR DE LOS DATOS
                        jungleBlue.innerHTML = data[index]["Jungle"];//AGREGAR VALOR DE LOS DATOS
                        midBlue.innerHTML = data[index]["Mid"];//AGREGAR VALOR DE LOS DATOS
                        shooterBlue.innerHTML = data[index]["Adc"];//AGREGAR VALOR DE LOS DATOS
                        supportBlue.innerHTML = data[index]["Support"];//AGREGAR VALOR DE LOS DATOS
                        break;
                    }
                }
            });
            d3.csv("./Data/ChampsPlayedByRedTeams.csv", function(data){
                for(index in data){
                    var team = data[index]["Team"];
                    if(team == redTeam){
                        TopRed.innerHTML = data[index]["Top"];//AGREGAR VALOR DE LOS DATOS
                        jungleRed.innerHTML = data[index]["Jungle"];//AGREGAR VALOR DE LOS DATOS
                        midRed.innerHTML = data[index]["Mid"];//AGREGAR VALOR DE LOS DATOS
                        shooterRed.innerHTML = data[index]["Adc"];//AGREGAR VALOR DE LOS DATOS
                        supportRed.innerHTML = data[index]["Support"];//AGREGAR VALOR DE LOS DATOS
                        break;
                    }
                }
            });
        }
    }
    else{
        //flag = true;    
    }
  }
  


