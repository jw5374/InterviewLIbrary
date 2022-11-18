// slow n^2
function commonChars(words) {
	let first = words.pop()
	let hash = letterFreq(first)
	let res = []
	for(let word of words) {
		let localhash = letterFreq(word)
		for(let key in localhash) {
			if(hash[key] == undefined) {
				delete localhash[key]
				continue
			}
			if(hash[key] < localhash[key]) {
				localhash[key] = hash[key]
			}
		}
		hash = localhash
	}
	return freqArray(hash)
}

function freqArray(freqHash) {
	let res = []
	for(let key in freqHash) {
		while(freqHash[key] > 0) {
			res.push(key)
			freqHash[key]--
		}
	}
	return res
}

function letterFreq(word) {
	let hash = {}
	for(let i = 0; i < word.length; i++) {
		let letter = word.charAt(i)
		if(hash[letter] != undefined) {
			hash[letter]++
		} else {
			hash[letter] = 1
		}
	}
	return hash
}

console.log(commonChars(["cool","lock","cook"]))
