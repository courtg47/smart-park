// JavaScript
$(document).ready(function() {

  // Reload page every 4 minutes
  window.setInterval('reloadPage()', 24000);

  function clock() {
    const date = new Date();
    let hours = date.getHours();
    const minutes = date.getMinutes();
    let seconds = date.getSeconds();
    let halfOfDay = "AM";

    // Converts military time to standard American time with AM and PM.
    if (hours == 0) {
      hours = 12;
    } else if (hours > 12) {
      hours = hours - 12;
      halfOfDay = "PM";
    }

    // Adds a 0 to the beginning of minutes and seconds
    minutes < 10 ? minutes = "0" + minutes : minutes;
    seconds < 10 ? seconds = "0" + seconds : seconds;

    // Actual time that will be appended to the screen
    const time = hours + ":" + minutes + ":" + seconds + " " + halfOfDay;

    $(".second-box").html(time);
  }

  setInterval(clock, 1000);

});

// Reload page
function reloadPage() {
    window.location.reload(true);
}
