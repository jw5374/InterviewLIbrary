function validMountainArray(arr) {
  if(arr.length < 3) {
    return false
  }
  let i = 0 
  while(i < arr.length-1 && arr[i] < arr[i+1]) {
    i++
  }
  if(arr[i] <= arr[i+1] || i == arr.length-1 || i == 0) {
    return false
  }
  while(i < arr.length-1 && arr[i] > arr[i+1]) {
    i++
  }
  if(i == arr.length - 1) {
    return true
  } else {
    return false
  }
}

console.log(validMountainArray([2,1,0]))
