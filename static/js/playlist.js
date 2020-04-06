$(".btn-like, .btn-dislike, .btn-playlist-add").on("click", function() {
    let urlFor;
    let toastMsg;
    let trackID = $(this).attr("id");  // get .btn ID (track._id)
    if ($(this).hasClass("btn-like")) {  // if clicking "LIKE" button
        // create url_for path
        urlFor = "{{ url_for('like', track_id='fakeID') }}".replace("fakeID", trackID);
        toastMsg = "You Like this Song!";
    } else if ($(this).hasClass("btn-dislike")) {  // if clicking "DISLIKE" button
        // create url_for path
        urlFor = "{{ url_for('dislike', track_id='fakeID') }}".replace("fakeID", trackID);
        toastMsg = "You Dislike this Song!";
    } else if ($(this).hasClass("btn-playlist-add")) {  // if clicking "ADD TO PLAYLIST" button
        urlFor = "{{ url_for('playlist_addto', track_id='fakeID') }}".replace("fakeID", trackID);
        toastMsg = "Song added to your Playlist!";
    };
    $.ajax({type: "POST", url: urlFor}).done(function () {  // ajax without page reload
        M.toast({html: toastMsg});  // flash message to user
    });
});

// This solution was inspired by https://github.com/Code-Institute-Submissions/dhamma1991-milestone-project-3/blob/master/templates/tracks.html
if ('{{ sorting_order }}' == 1) {
    $('.dropdown-trigger span').text("Most Liked");
} else if ('{{ sorting_order }}' == 2) {
    $('.dropdown-trigger span').text("Most Disliked");
} else if ('{{ sorting_order }}' == 3) {
    $('.dropdown-trigger span').text("Newest");
} else if ('{{ sorting_order }}' == 4) {
    $('.dropdown-trigger span').text("Oldest");
}