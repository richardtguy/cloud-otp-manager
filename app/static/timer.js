function startTimer(t) {
  var progressBarAnimation = document.getElementById('countdown').animate(
    [
      { width: 100 * (t / 30000) + '%' },
      { width: '0%' }
    ],
    {
      duration: t
    });
  setTimeout("location.reload(true);", t);
}
