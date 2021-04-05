$(document).ready(function () {
    console.log('hello world')
    $('#modal-btn').click(function () {
        console.log('working')
        $('.modal')
            .modal('show')
            ;
    })
    $('.ui.dropdown').dropdown()
})