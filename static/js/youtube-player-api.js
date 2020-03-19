    // create playList array with each song ID
    let playList = []
    {% for song in users.playlist %}
        playList.push("{{song}}");
    {% endfor %}

    var tag = document.createElement('script');
    tag.id = 'iframe-demo';
    tag.src = 'https://www.youtube.com/iframe_api';
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

    var player;

    function onYouTubeIframeAPIReady() {
        player = new YT.Player('player', {
            videoId: playList[0],
            playerVars: {
                'autoplay': 1,
                'controls': 1
            },
            events: {
                'onReady': onPlayerReady,
                'onStateChange': onPlayerStateChange
            }
        });
    }

    function onPlayerReady(event) {
        document.getElementById('player').style.border = '5px solid #e487d8';
    }

    function onPlayerStateChange(event) {
        if (event.data == YT.PlayerState.ENDED) {
            $("#" + playList[0]).hide(); // hide the first song from 'upcoming' list
            playList.shift(); // remove first song from playList array
            if (playList.length != 0) {
                // play the next video in the playlist
                player.loadVideoById(playList[0]);
            } else {
                // auto-call @app.route('/catalogue')
                window.location.href = "/catalogue";
            }
        } else {
            // show which song is currently playing
            $("#" + playList[0] + " .current").text("(Currently Playing)");
        }
    }