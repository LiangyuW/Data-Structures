//return the longest word in a string

function LongestWord(sen) {
    var longest =""
    let count = 0
    let j=0
    for(let i=0; i<sen.length; i++) {
        if(sen[i] != " ") {
            j++
        } else {
            if(j > count) {
                count = j
                longest = sen.substring(i-j, i)
            
            }
            j=0
        }
    }
    return longest
}

console.log(LongestWord("The culmination of the progressionist speech for which I labored was often criticism, bored expressions, and, sometimes, outright rejection; thus, after unsuccessful revisions and heartfelt considerations, I came to a conclusion: no radical idea, however expertly or clumsily delivered and written, will be unanimously accepted; instead, radical ideas will often encounter criticism without constructive comment, but this fact does not negate our responsibility to write them and take a stand."))