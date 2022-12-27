/* set up default csrf token cookie 
$(document).ready(function(){
$.ajaxSetup({
    data:{
        csrfmiddlewaretoken: '{{ csrf_token }}',
    },
});
});
*/



$('.search-box').bind('input propertychange',function(){
    if ((this).value.trim()){
    $.ajax({
        url:'ajax/',
        type:'GET',
        dataType:'json',
        data:{'search_name':$('.search-box').val()},
        success:function(context){
            $(".searching-result-num").html('Num of records: '+context.count)
        },

    });}
    else{
        $('.searching-result-num').text('');
    };

});    

/*
used for user history
$('.displayed-items').click(function(){
    $.ajax({
        url:'history/',
        typeL:'GET',
        dataType:'json',
        data:{
                'clicked_videopage' : $('.displayed-items p').text(),
        },
        success:function(){
            return true
            },
    })
});
*/
