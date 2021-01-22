function getData(){
    d3.csv("./Data/matches2020.csv", (data)=>{
        console.log(data)
    });
}