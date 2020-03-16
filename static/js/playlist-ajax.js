$(document).ready(function() {
        $('.Button1').on('click', function() {

            var track_id = $(this).attr('track_id');
            console.log(track_id);

            req = $.ajax({
                url : '/playlist_addto',
                type : 'POST',
                data : {track_id : track_id}
            });

            event.preventDefault();
        });
    });