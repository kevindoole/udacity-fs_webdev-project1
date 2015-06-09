// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $("#trailer-video-container").empty();
});

// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.movie-tile', function (event) {
    var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
    var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
    $("#trailer-video-container").empty().append($("<iframe></iframe>", {
      'id': 'trailer-video',
      'type': 'text-html',
      'src': sourceUrl,
      'frameborder': 0
    }));
});

// Animate in the movies when the page loads
$(document).ready(function () {
  $('.movie-tile').hide().first().show("fast", function showNext() {
    $(this).next("div").show("fast", showNext);
  });

  $('.movie-tile').each(function(index) {
    var $t = $(this);
    var title = $t.find('h2').text();
    title = title.replace(' ', '+');
    $.getJSON('http://www.omdbapi.com/?t=' + title + '&y=&plot=short&r=json&tomatoes=true', function(data) {
      var moreInfo = data.Plot + '<br />' +
        'IMDB Rating: ' + data.imdbRating + '<br />Rotten tomatoes: ' + data.tomatoRating + '</p>';
      $t.find('.more-info').addClass('loaded').append(moreInfo);
    });
    $(this).append();
  });
});