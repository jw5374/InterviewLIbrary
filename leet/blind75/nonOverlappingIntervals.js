function eraseOverlapIntervals(intervals) {
	intervals.sort((a,b) => a[0] - b[0])
	let result = 0
	for(let i = 0; i < intervals.length-1; i++) {
		let j = i+1
		while(j < intervals.length && intervals[j][0] != null && intervals[i][0] != null && (intervals[i][0] == intervals[j][0] ||
			intervals[i][1] > intervals[j][0] ||
			(intervals[i][0] < intervals[j][0] && intervals[i][1] > intervals[j][1]))
	) {
			result++
			if(intervals[i][1] > intervals[j][1]) {
				intervals[i][0] = null
				intervals[i][1] = null
				i++
			} else {
				intervals[j][0] = null
				intervals[j][1] = null
			}
			j++
		}
	}
	return result
}

console.log(eraseOverlapIntervals([[-8,56],[29,31],[96,100],[-62,-49],[-97,55],[94,99],[-32,-3],[98,99],[-59,-3],[21,92],[-3,89],[-20,26],[-39,33],[85,97],[11,21],[-81,13],[-47,-14],[-40,16],[-85,-6],[60,62],[-89,-70],[71,93],[29,91],[80,86],[-8,82],[-1,27],[14,32],[-67,32],[-67,-53],[91,97],[30,91],[52,75],[-22,63],[-76,-51],[-22,3],[91,97],[-65,55],[18,33],[24,88],[85,92],[97,99],[-21,21],[3,45],[37,78],[84,88],[-87,58],[-50,-38],[57,81],[-10,81]]))
