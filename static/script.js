function overTimer() {
  if (typeof(Storage) !== "undefined") {
    if (sessionStorage.timecount) {
      sessionStorage.timecount = Number(sessionStorage.timecount)+1;
    } else {
      sessionStorage.timecount = 1;
    }
    document.getElementById("result").innerHTML = sessionStorage.timecount
  }	else {
	  document.getElementById("result").innerHTML = "Sorry, your browser does not support web storage...";
  }
}