function addComment(post_id, name, quest, color, message){
    $.ajax({
        url: "/blog/api/comment/",
        type: 'POST',
        data: {
            'csrfmiddlewaretoken':'{{csrf_token}}',
            'post_id':post_id,
            'name':name,
            'quest':quest,
            'color':color,
            'message':message
        },
        dataType:"json",
        success: function( data ) {
            setTimeout(function(){
                // I could probably just reload the part where the comments are
                // Actually that would have been the whole point of using Ajax.
                location.reload();
            }, 200);    // Let's wait for the server to be finished with the transaction. Arbitrary 200ms
        }
    });
};

function submitComment(id){
    console.log("adding")
    // well I guess I could check if those are empty or SQL stuff or anything.
    addComment( id, $("#nameF").val(), $("#questF").val(), $('input[name=color]:checked').val(), $("#messageF").val());
    $("input").val('');
    $("#messageF").val('')
};