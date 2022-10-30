const { ListNode } = require('./mergeSortedLinkedList.js')

function hasCycle(head) {
    if(head == null) {
        return false
    }
    let iter = head
    while(head.next != null) {
        head.val = null
        if(head.next.val == null) {
            return true
        }
        head = head.next
    }
    return false
}

function createCycle(arr, pos = -1) {
  if(arr.length == 0) {
    return null
  }
  let list = new ListNode()
  let listH = list
  let cycleNode
  for(let i = 0; i < arr.length; i++) {
    list.val = arr[i]
    if(i == pos) {
      cycleNode = list
    }
    if(i == (arr.length - 1) && pos != -1) {
      list.next = cycleNode
      break
    } else if(i == (arr.length - 1) && pos == -1) {
      break
    }
    list.next = new ListNode()
    list = list.next
  }
  return listH
}

let linked = createCycle([3,2,0,-4], 1)

console.log(linked)
console.log(hasCycle(linked))
