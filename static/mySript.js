// CountDown
// const number= 20
// let count = number
// function countdown(){
//     document.getElementById('number').innerHTML = count
//     count--
//     if (count < 0){
//         clearInterval(interval)
//     }
// }
// countdown()
// const interval = setInterval(countdown,1000)

// let englishWord = "{{current_english_word}}"
// let vietnamWord = '{{current_vietnam_word}}'

// document.getElementById('wordsToTranslate').innerHTML = vietnamWord

let doc = Jsoup.connect("https://dictionary.cambridge.org/vi/").get();
log(doc.title());

