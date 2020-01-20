function display_datetime() {
    var datetime = new Date()
    weekday = new Array(7)
    weekday[0] = "Sonntag";
    weekday[1] = "Montag";
    weekday[2] = "Dienstag";
    weekday[3] = "Mittwoch";
    weekday[4] = "Donnerstag";
    weekday[5] = "Freitag";
    weekday[6] = "Samstag";
    var month = datetime.getMonth() + 1
        h = clearNr(datetime.getHours())
        m = clearNr(datetime.getMinutes())
    document.getElementById("ct").innerHTML = h + ":" + m; 
    document.getElementById("dt").innerHTML = weekday[datetime.getDay()] + ", " + datetime.getDate() + "." + month + "." + datetime.getFullYear();
    var refresh=500;
    mytime=setTimeout(display_datetime, refresh)
}

function clearNr(n) {
    // checks the number format
    if (n < 10) {
        return "0"+n
    }
    return n
}