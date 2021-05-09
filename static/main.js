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

$('#exampleModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    var recipient = button.data('whatever') // Extract info from data-* attributes
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $(this)

    modal.find('.modal-body #bookId').val(recipient)
})

$(document).on('click', '#like-button', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '{% url "like" %}',
        data: {
            postid: $('#like-button').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success: function (json) {
            document.getElementById("favourite").innerHTML = json['application']
            console.log('working')
        },
        error: function (xhr, errmsg, err) {

        }
    });
})


$(function () {
    $('#datetimepicker1').datetimepicker();
});