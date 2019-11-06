
var getPredict = d3.select("#getPrediction")
getPredict.on("click",function(){
var departureAirport = d3.select("#dropdownDeparture").property("value")
var destinationAirport = d3.select("#dropdownDestination").property("value")
var travelDate = d3.select("#travelDate").property("value")
console.log(departureAirport)
console.log(destinationAirport)
console.log(travelDate)

/*
departureAirport = request.args.get('departureAirport')
    arrivalAirport = request.args.get('arrivalAirport')
    date = request.args.get('departureDate')
*/
// d3.json('/getPrediction', {
//       method:"POST",
//       body: JSON.stringify({
//         departureAirport: departureAirport,
//         arrivalAirport: destinationAirport,
//         departureDate: travelDate
//       }),
//       headers: {
//         "Content-type": "application/json; charset=UTF-8"
//       }
//     })
//     .then(function(data){
//         console.log(data)
//     });

var plotData = `/getPredictions/${departureAirport}`;

//d3.json(`/getPrediction/?departureAirport=${departureAirport}&arrivalAirport=${destinationAirport}&departureDate=${travelDate}`).then(function(sampledata){
d3.json(plotData).then(function(data){ 
    console.log('@@@@@@')
    console.log(data)
});
})



function init() {
    ["#dropdownDeparture","#dropdownDestination"].forEach(function(x){
        // Grab a reference to the dropdown select element
        var selector = d3.selectAll(x);
        console.log("#############")
        console.log("inside init" + selector) 

        // Use the list of sample names to populate the select options
        d3.json("/airportIDs", (sampleNames) => {
        console.log(sampleNames) 
        sampleNames.forEach((sample) => {
            selector
            .append("option")
            .text(sample)
            .property("value",sample);
        });

  
      // Use the first sample from the list to build the initial plots
      

    });
    })
    

  }



// Initialize the dashboard
init();
