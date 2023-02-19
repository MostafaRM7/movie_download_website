if($(".DashSlider") != null)
{
 $(".DashSlider").slick({
     arrows : false,
     slidesToShow: 4,
     variableWidth : true,
     slidesToScroll: 4,
     responsive: [   
     {
   breakpoint: 1080,
   settings: {
       slidesToShow: 3,
       slidesToScroll: 3,
   }
 },
{
   breakpoint: 768,
   settings: {
       slidesToShow: 2,
       slidesToScroll: 2,
   }
 },
 {
   breakpoint: 500,
   settings: {
       slidesToShow: 1,
       slidesToScroll: 1,
   }
 }
]
 
 })
}
if($(".cartoon-slider") != null)
{
 $(".cartoon-slider").slick({
     arrows : false,
     slidesToShow: 2,
     autoplay: true,
     autoplaySpeed: 1000,
     variableWidth : true,
     slidesToScroll: 1,
     
     responsive: [   
     {
   breakpoint: 1080,
   settings: {
       slidesToShow: 3,
       slidesToScroll: 2,
   }
 },
 {
   breakpoint: 500,
   settings: {
       slidesToShow: 3,
       slidesToScroll: 1,
       autoplaySpeed: 1800
     }
   }
 ]
 })
}
if($(".recentSeries-slider") != null)
{
    $(".recentSeries-slider").slick({
        autoplay: true,
        variableWidth : true,
        infinite: true,
        slidesToShow : 5,
        slidesToScroll : 3,
        centerMode: true,
        arrows : false,
        autoplaySpeed: 1200,
    })
    responsive: [   
         {
             breakpoint: 500,
           settings: {
               autoplaySpeed: 1800
           }
         }
        ]
}
if($(".Catitems") != null)
{
    $(".Catitems").slick({
        arrows : false,
        infinite: true,
        slidesToShow: 4,
        slidesToScroll: 3,
        variableWidth : true,
    })
}
if($(".regular") != null)
  $(".regular").slick({
   infinite: true,
   centerMode: true,
   arrows : false,
   slidesToShow: 4,
   autoplay: false,
   slidesToScroll: 3,
   centerMode: false,
   swipeToSlide : true,
   variableWidth : true,
   adaptiveHeight: true,
   responsive: [   
{
   breakpoint: 768,
   settings: {
       slidesToShow: 2,
       slidesToScroll: 2
   }
 },
 {
     breakpoint: 500,
   settings: {
       slidesToShow: 1,
       slidesToScroll: 1,
   }
 }
]
 });