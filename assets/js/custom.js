function show_password() {
    let pass_input = document.getElementById('pass-input')
    if (pass_input.type === 'password') {
        pass_input.type = 'text'
    } else {
        pass_input.type = 'password'
    }

}

function set_wall(id) {
    switch (id) {
        case 1:
            $("#" + id).attr('class', 'bg-Image')
            $("#2").attr('class', 'hide')
            $("#3").attr('class', 'hide')
            $("#4").attr('class', 'hide')
            $("#5").attr('class', 'hide')
            break;

        case 2:
            $("#" + id).attr('class', 'bg-Image')
            $("#1").attr('class', 'hide')
            $("#3").attr('class', 'hide')
            $("#4").attr('class', 'hide')
            $("#5").attr('class', 'hide')
            break;

        case 3:
            $("#" + id).attr('class', 'bg-Image')
            $("#1").attr('class', 'hide')
            $("#2").attr('class', 'hide')
            $("#4").attr('class', 'hide')
            $("#5").attr('class', 'hide')
            break;

        case 4:
            $("#" + id).attr('class', 'bg-Image')
            $("#1").attr('class', 'hide')
            $("#2").attr('class', 'hide')
            $("#3").attr('class', 'hide')
            $("#5").attr('class', 'hide')
            break;

        case 5:
            $("#" + id).attr('class', 'bg-Image')
            $("#1").attr('class', 'hide')
            $("#2").attr('class', 'hide')
            $("#4").attr('class', 'hide')
            $("#3").attr('class', 'hide')
            break;
        default:
            break;

    }
}
function remove_from_favorite(slug) {
    console.log(slug)
    $.ajax({
        url: '../../user/remove-favorite-movie/?slug=' + slug,
        type: 'GET',
        success: function (data) {
            if (data.success == true) {
                $("#favorite").attr('class', 'bi-bookmark-plus')
                $("#favorite").attr('onclick', 'add_to_favorite("' + slug + '")')
            }
        }
    })
}

function add_to_favorite(slug) {
    console.log(slug)
    $.ajax({
        url: '../../user/favorite-movie/?slug=' + slug,
        type: 'GET',
        success: function (data) {
            if (data.success == true) {
                $("#favorite").attr('class', 'bi-bookmark-plus-fill')
                $("#favorite").attr('onclick', 'remove_from_favorite("' + slug + '")')
            }
        }
    })
}

function hide_element(id) {
    let element = document.getElementById(id)
    element.style.display = 'none'
}
function show_element(id) {
    let element = document.getElementById(id)
    element.style.display = 'block'
}