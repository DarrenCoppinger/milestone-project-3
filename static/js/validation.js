var form = document.getElementsByTagName('form')[0],
    track = document.getElementById('track_name'),
    artist = document.getElementById('artist_name'),
    year = document.getElementById('year'),
    genre = document.getElementById('genre_name'),
    lyrics = document.getElementById('lyrics_link'),
    video = document.getElementById('video_link');

/* Below solution found here on Stackoverflow: https://stackoverflow.com/questions/28735459/how-to-validate-youtube-url-in-client-side-in-text-box */
function validateYouTubeUrl() {
    var url = $('#video_link').val();

    if (url != undefined || url != '') {
        var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=|\?v=)([^#\&\?]*).*/;
        var match = url.match(regExp);
        if (match && match[2].length == 11) {
            // alert(match[2]);
            $('#video_link').attr('value', match[2]);
        } else {
            $("#video_link").removeClass("valid");
            $("#video_link").addClass("invalid");
            $("#video_link_label").addClass("active");
            $("#video_link").prop("aria-invalid", "true");
            event.preventDefault();
        }
    }
}

/*original code credit: "https://github.com/Code-Institute-Submissions/dhamma1991-milestone-project-3/" */
form.addEventListener("submit", function (event) {
    if (!track.validity.valid) {
        $("#track_name").removeClass("valid");
        $("#track_name").addClass("invalid");
        $("#track_name_label").addClass("active");
        $("#track_name").prop("aria-invalid", "true");
        event.preventDefault();
    }

    if (!artist.validity.valid) {
        $("#artist_name").removeClass("valid");
        $("#artist_name").addClass("invalid");
        $("#artist_name_label").addClass("active");
        $("#artist_name").prop("aria-invalid", "true");
        event.preventDefault();
    }

    if (!year.validity.valid) {
        $("#year").removeClass("valid");
        $("#year").addClass("invalid");
        $("#year_label").addClass("active");
        $("#year").prop("aria-invalid", "true");
        event.preventDefault();
    }

    if (!genre.validity.valid) {
        $("#genre_name").removeClass("valid");
        $("#genre_name").addClass("invalid");
        $("#genre_name_label").addClass("active");
        $("#genre_name").prop("aria-invalid", "true");
        event.preventDefault();
        $('select').material_select();
    }

    if (!lyrics.validity.valid) {
        $("#lyrics_link").removeClass("valid");
        $("#lyrics_link").addClass("invalid");
        $("#lyrics_link_label").addClass("active");
        $("#lyrics_link").prop("aria-invalid", "true");
        event.preventDefault();
    }

    validateYouTubeUrl();
}, false);

