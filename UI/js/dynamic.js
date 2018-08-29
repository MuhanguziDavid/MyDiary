function setReminderField() {
    var x = document.createElement("INPUT");
    x.setAttribute("type", "date");
    x.setAttribute("id", "dateField");

    x.style.position = 'absolute';
    x.style.top = '66%';
    x.style.left = '44.5%';

    document.body.appendChild(x);
}