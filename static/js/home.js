console.log("loaded")




document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(elems, {edge:"right"});
});




document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.slider');
    var instances = M.Slider.init(elems, {'height' : 750, 'interval': 60000, 'indicators' : true});

  
  });

  M.AutoInit();



  




  // function myFunction() {
  //   location.replace("https://www.w3schools.com")
  // }