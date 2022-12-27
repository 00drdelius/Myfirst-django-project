function getComment(){
    $(document).ready(function(){
        $.ajax({
            url:"{% url 'full_test:ajax_getComment' id=video_displayed.videoID.int %}",
            type:'GET',
            success:function(data){
                $('.user-comment-display-area').html(data);
            },
            error:function(data){
                console.log('ajax_getComment failed');
            },
        });
    });
};
getComment();  /* render the comments as long as the DOM tree loaded. */
$('.comment-submit-button').click(function(){
    if($('.your-comment-place').val()){
        $.ajax({
            url:"{% url 'full_test:ajax_comment' id=video_displayed.videoID.int %}",
            /*url:'ajax/comment/',*/
            type:'POST',
            dataType:'json',
            data:{
                csrfmiddlewaretoken: '{{ csrf_token }}',
                'user_comment': $('.your-comment-place').val(),
            },
            beforeSend:function(){
                console.log('ready to send to url ajax_comment');
            },
            success:function(data){
                console.log('comment_ajax request succeed!');
                if(data.status =='success'){
                    getComment();
                };
            },
        });
    };
});