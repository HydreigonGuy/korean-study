
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

    var word_info = "";
    var correct = false;
    var kr_list = []
    for (let k_word in word.korean) {
        if (word.korean[k_word].word == input)
            correct = true;
        kr_list.push(word.korean[k_word].word)
    }
    if (correct)
        word_info = "O"
    else
        word_info = "X"
    word_info = word_info + " - " + word.word + ": " + kr_list.join(', ') + "<br/>";
    document.getElementById("previous-words").innerHTML = word_info + document.getElementById("previous-words").innerHTML;
    document.getElementById("input").value = "";
    get_word();
}

window.onload = function(e){
    get_word();
}
