function removePost(post_id){
    $.ajax({
        url: "/blog/api/articles/"+post_id,
        type: 'POST',
        data: {'csrfmiddlewaretoken':'{{csrf_token}}'},
        dataType:"json",
        success: function( data ) {
            setTimeout(function(){
                location.reload();
            }, 200);    // Let's wait for the server to be finished with the transaction. Arbitrary 200ms
        }
    });
}

function removeComment(id){
    $.ajax({
        url: "/blog/api/comment/delete",
        type: 'POST',
        data: {
            'csrfmiddlewaretoken':'{{csrf_token}}',
            'comment_id':id,
        },
        dataType:"json",
        success: function( data ) {
            setTimeout(function(){
                location.reload();
            }, 200);
        }
    });
};