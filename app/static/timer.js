function autoRefresh(t) {
  console.log(t / 1000)
  setTimeout("location.reload(true);", t);
}
