var textInside_h1 = "A day at the mall";
var textInside_p = "Yesterday was an unusual day for me. I spent the morning with a dear childhood friend who was visiting from abroad for a few days. She had brought a shopping list with her, so off we went to a large local mall, to get the items she was looking for. This was a great opportunity for us to catch up and reminisce about our common past. We walked the mall levels from end to end, and by lunchtime we were starved. The food courtyard seemed the most logical lunch spot. You probably know that mall food courts are not exactly made for the health-conscious crowd. Everywhere we looked, there were burgers, deli sandwiches, french fries, and ice cream parlors. My friend is also following the Save Our Bones Program, so putting together our bone-healthy lunch seemed a little challenging. Luckily, we spotted a “Build-Your-Salad” counter, somewhat hidden from the main area at the far corner of the giant food court. Perfect! Not only do I love salads, I also strive to eat raw foods as much as possible And that’s exactly what we did: we “built” our salads with lots of alkalizing fresh goodies and crunchy toppings. I stacked my salad.";

function entryContents_getTextFromEntry() {
    textInside_h1 = ctrl.getElementById('h1_entryTitle')[0].innerHTML;
}

function editEntry_autofillEntryFields() {
    document.getElementById('inputTitle').value = textInside_h1;
    document.getElementById('textareaDetails').value = textInside_p;
}

function setReminderField() {
    var x = document.createElement("INPUT");
    x.setAttribute("type", "date");
    x.setAttribute("id", "dateField");

    x.style.position = 'absolute';
    x.style.top = '66%';
    x.style.left = '44.5%';

    document.body.appendChild(x);
}