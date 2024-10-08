
var word;

function get_word(prev={}) {
    var url = "/get-word"

    if (!(Object.keys(prev).length === 0)) {
        url = url + "?word=" + prev.word
        if (prev.success)
            url = url + "&res=true"
        else
            url = url + "&res=false"
    }
    fetch(url)
    .then(response => response.json())
    .then(function (body) {
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
        word_info = "<span class='correct'>O</span>"
    else
        word_info = "<span class='wrong'>X</span>"
    word_info = word_info + " - " + word.word + ": " + kr_list.join(', ') + "<br/>";
    document.getElementById("previous-words").innerHTML = word_info + document.getElementById("previous-words").innerHTML;
    document.getElementById("input").value = "";
    get_word({"word": word.word, "success": correct});
}

window.onload = function(e){
    get_word();
}
