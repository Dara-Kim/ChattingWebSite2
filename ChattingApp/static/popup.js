$('area').each(function(){
    var area = $(this),
        alt = area.attr('alt');
    area.mouseenter(function(){
        $('#overlay').html(alt);
    }).mouseleave(function(){
        $('#overlay').html('');
    });
});