var form = document.getElementsByTagName('form')[0],
    track_name = document.getElementById('track_name'),
    video_link = document.getElementById('video_link');
/* Below solution found here on Stackoverflow: https://stackoverflow.com/questions/28735459/how-to-validate-youtube-url-in-client-side-in-text-box */
function validateYouTubeUrl() {
    var url = $('#video_link').val();

    if (url != undefined || url != '') {
        var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=|\?v=)([^#\&\?]*).*/;
        var match = url.match(regExp);
        if (match && match[2].length == 11) {
            // alert(match[2]);
            $('#video_link').attr('value', 'https://www.youtube.com/embed/' + match[2] + '?autoplay=1');
        } else {
            $("#video_link").removeClass("valid");
            $("#video_link").addClass("invalid");
            $("#video_link").addClass("active");
            $("#video_link").prop("aria-invalid", "true");
            event.preventDefault();
        }
    }
}

form.addEventListener("submit", function (event) {
    if (!track_name.validity.valid) {
        $("#track_name").removeClass("valid");
        $("#track_name").addClass("invalid");
        $("#track_name_label").addClass("active");
        $("#track_name").prop("aria-invalid", "true");
        event.preventDefault();
    }
    
    validateYouTubeUrl();

}, false);