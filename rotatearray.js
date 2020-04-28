
//rotate an array

function rotateArray(ary, k) {
    newary = []
    j = ary.length
    for(i=j-k%j; i< j; i++){
        newary.push(ary[i])
    }

    for(i=0; i<j-k%j; i++){
        newary.push(ary[i])
    }

    return newary
}

console.log(rotateArray([1,2,5,6,9], 1301))