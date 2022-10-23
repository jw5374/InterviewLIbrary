/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
 
function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : next)
}
 
function mergeTwoLists(list1, list2) {
  if(list1 == null && list2 == null) {
    return null
  }
  if(list1 == null) {
    return list2
  }
  if(list2 == null) {
    return list1
  }
  let head1 = list1
  let head2 = list2
  let result = new ListNode()
  let resultH = result
  while(true) {
    if(head1 != null) {
      if(head2.val > head1.val) {
        result.val = head1.val
        head1 = head1.next
      } else {
        result.val = head2.val
        head2 = head2.next
      }
    } else {
      result.val = head2.val
      head2 = head2.next
    }
    if(head2 == null) {
      break
    }
    result.next = new ListNode()
    result = result.next
  }
  while(head1 != null) {
    result.next = new ListNode()
    result = result.next
    result.val = head1.val
    head1 = head1.next
  }
  return resultH
}

function createLinked(arr) {
  if(arr.length == 0) {
    return null
  }
  let list = new ListNode()
  let listH = list
  for(let i = 0; i < arr.length; i++) {
    list.val = arr[i]
    console.log(arr[i], list.val, list, listH)
    if(i == (arr.length - 1)) {
      break
    }
    list.next = new ListNode()
    list = list.next
  }
  return listH
}

function printLinked(linkedList) {
  let res = []
  if(linkedList == null) {
    return res
  }
  while(linkedList != null) {
    res.push(linkedList.val)
    linkedList = linkedList.next
  }
  return res
}

let list1 = [1,2,4]
let list2 = [1,3,4]
let linked1 = createLinked(list1)
let linked2 = createLinked(list2)

let merged = mergeTwoLists(linked1, linked2)
console.log(printLinked(merged), printLinked(linked1), printLinked(linked2))
