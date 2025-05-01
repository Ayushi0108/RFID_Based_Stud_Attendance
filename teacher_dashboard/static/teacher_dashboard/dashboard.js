// start of navebar code for responsive header
const nav = document.querySelector(".primary-navigation");
const navToggle = document.querySelector(".mobile-nav-toggle");

navToggle.addEventListener("click", () => {
    
    const visiblity = nav.getAttribute("data-visible");
    if (visiblity === "false") {
        nav.setAttribute("data-visible", true);
        navToggle.setAttribute("aria-expanded", true);
    } else {
        nav.setAttribute("data-visible", false);
        navToggle.setAttribute("aria-expanded", false);
    }
})
// end for nave bar code 


// ************************ //

// code for Graph
// window.onload = function () {

//     var chart = new CanvasJS.Chart("chartContainer", {
//         animationEnabled: true,
//         theme: "light2",
//         title:{
//             text: "Simple Line Chart"
//         },
//         data: [{        
//             type: "line",
//               indexLabelFontSize: 16,
//             dataPoints: [
//                 { y: 450 },
//                 { y: 414},
//                 { y: 520, indexLabel: "\u2191 highest",markerColor: "red", markerType: "triangle" },
//                 { y: 460 },
//                 { y: 450 },
//                 { y: 500 },
//                 { y: 480 },
//                 { y: 480 },
//                 { y: 410 , indexLabel: "\u2193 lowest",markerColor: "DarkSlateGrey", markerType: "cross" },
//                 { y: 500 },
//                 { y: 480 },
//                 { y: 510 }
//             ]
//         }]
//     });
//     chart.render();
// }
// end of graph code

