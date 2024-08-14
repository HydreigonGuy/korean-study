
var word;

function get_word() {
    fetch("/get-word")
    .then(response => response.json())
    .then(function (body) {
        console.log(body);
        word = body;
        document.getElementById("word").innerHTML = word.word;
    })
}

function check() {
    const input = document.getElementById("input").value;

    console.log(input);
}
