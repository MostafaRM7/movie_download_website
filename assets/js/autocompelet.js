const searchinput = document.getElementById("searchinput");

searchinput.addEventListener("input", (e) => {
    fetch('/search/?movie=' + e.target.value)
        .then(response => response.json())
        .then(data => {
            $(function () {
                $("#searchinput").autocomplete({
                    source: data,
                    minLength: 1,
                    select: function (event, ui) {
                        location.href = ui.item.url;
                        console.log("selected")
                    },
                    html: true,
                    hover :  function(event,ui)
                    {
                        console.log("hover")
                    },
                    open: function (event, ui) {
                       
                        // $('.ui-autocomplete').off('menufocus hover mouseover mouseenter');
                        $('.ui-autocomplete').unbind("hover mouseover mouseenter")
                        $(".ui-autocomplete").appendTo($(".searchBox"))
                        $(".ui-autocomplete").css("z-index", 1000);
                        
                    }
                })
                    .autocomplete("instance")._renderItem = function (ul, item) {
                    return ($("<li><div><div class = SearchItemEffect></div>  <img src='" + item.img + "'><span>" + item.label + "</span></a></div></li>").appendTo(ul));
                };

            });
        })
})
