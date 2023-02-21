var NavMenuToggle = document.querySelector("nav .ToggleButton button");
var navButtons = document.querySelectorAll("nav .navbarList .navbarItem a");
var LoginButton = document.querySelector(".LoginButt");

// Navbar Toogle Button
NavMenuToggle.addEventListener(
    "click",
    () => {
    $(".navbarList").slideToggle();
    NavMenuToggle.classList.toggle("active");
    
    if(NavMenuToggle.classList.contains("active"))
     $(".nav-mask").fadeIn(200);
    else
     $(".nav-mask").fadeOut(200);
  })
   $(".nav-mask").on(
    "click",
    () => {
    $(".navbarList").slideUp();
    NavMenuToggle.classList.remove("active");
    $(".nav-mask").fadeOut(200);
  })
    if(!NavMenuToggle.classList.contains("active"))
    $(".nav-mask").css("display","none");
  window.addEventListener("resize",() => {
    $(".navbarList").removeAttr("style");
    NavMenuToggle.classList.remove("active");
  })
  
  //contact us nav item eventlistener
  document.querySelectorAll(".navbarList .navbarItem")[3].addEventListener("click",() => {
    document.querySelector("footer").scrollIntoView();
    if(window.innerWidth < 950)
    {
      $(".navbarList").slideUp();
      NavMenuToggle.classList.remove("active");
      $(".nav-mask").fadeOut(200);
    }
    
  })