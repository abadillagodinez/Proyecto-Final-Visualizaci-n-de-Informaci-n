//Variables globales
//----------------------------------------------------




//----------------------------------------------------
//Se precargan los datos para almacenarlos en variables
//----------------------------------------------------
function ocultar(){
    document.getElementById('seleccionar').style.display = 'none';
  }

function getData(){
    d3.csv("./Data/WorldsTeamStats_FINAL.csv", (data)=>{
        console.log(data)
    });
}

function visParCoords(){
  document.getElementById("container").innerHTML = "";
  document.getElementById("grid").innerHTML = "";
  document.getElementById('container').setAttribute( "class", "parcoords" );
  document.getElementById('grid').setAttribute( "class", "scrollable" );
    //se generan las lineas del grafico con el color seleccionado
    var parcoords = d3.parcoords()("#container")
    .lineWidth(1)
    .alpha(0.7);

    var blueToRed = ["#13a5de","#e42d29"]

    d3.csv("./Data/champ_stats_w_winRate_FINAL.csv", function(data){
        //filtra las llaves que son numericas para obtener la primera
        var numericKeys = d3.keys(data[0]).filter(function(d){ //d is the key
            var valuesByKey = data.map(x=>x[d]);
            var keyType = (valuesByKey.some(isNaN) ? "categorical" : "numeric");
            if(keyType == "numeric"){
              return d;
            };  
          });
        var firstNumericKey = numericKeys[0]; //llave de la primera columna numerica
        parcoords
            .data(data)
            .render()
            .reorderable()
            .brushMode("1D-axes")
            .interactive();
        
        change_color(firstNumericKey,parcoords.data());

        var grid = d3.divgrid();
        d3.select("#grid")
          .datum(data)
          .call(grid)
          .selectAll(".row")
          .on({
            "mouseover": function (d) { parcoords.highlight([d]); },
            "mouseout": parcoords.unhighlight
          });

          parcoords.on("brush", function (d) {
            d3.select("#grid")
              .datum(d)
              .call(grid)
              .selectAll(".row")
              .on({
                "mouseover": function (d) { parcoords.highlight([d]); },
                "mouseout": parcoords.unhighlight
              });
          });

        
    });

    // update color
    function change_color(dimension,data) {
        //filtra las llaves que son numericas para obtener la primera
        var numericKeys = d3.keys(data[0]).filter(function(d){ //d is the key
        var valuesByKey = data.map(x=>x[d]);
        var keyType = (valuesByKey.some(isNaN) ? "categorical" : "numeric");
        if(keyType == "numeric"){
            return d;
        };  
        });
        if(numericKeys.includes(dimension)){
        parcoords.svg.selectAll(".dimension")
            .style("font-weight", "normal")
            .filter(function(d) { return d == dimension; })
            .style("font-weight", "bold")
        var actualNumericColumn = data.map(x=>x[dimension]).map(returnFloat);
        var maxIndex = Math.min(...actualNumericColumn); //valor minimo de esa columna
        var minIndex = Math.max(...actualNumericColumn); //valor maximo de esa columna
        var pltt_1 = d3.scale.linear()
            .domain([minIndex, maxIndex])
            .range(blueToRed)
            .interpolate(d3.interpolateLab);

        var clr = function (d) { return pltt_1(d[dimension])};

        parcoords.color(clr).render()
        } else {
        alert("No se puede colorear con esta columna, uno o más datos no son numéricos");
        }
    }

    //funcion para mapear a enteros
    function returnFloat(element){
        return parseFloat(element,10);
    }
}

