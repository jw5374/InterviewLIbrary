class MinStack {
  constructor() { 
    this.content = []
    this.min = []
  }
  push(item) {
   if(this.min.length == 0) {
     this.content.push(item)
     this.min.push(item)
     return
   }
   if(this.min[this.min.length-1] >= item) {
     this.content.push(item)
     this.min.push(item)
     return
   }
   this.content.push(item)
  }
  
  pop() {
    let popped = this.content.pop()  
    if(popped == this.min[this.min.length-1]) {
      this.min.pop()
    }
    return popped
  }
  
  top() {
    return this.content[this.content.length-1]
  }
  
  getMin() {
    return this.min[this.min.length-1]
  }
}

let stack = new MinStack()

stack.push(-2);
stack.push(0);
stack.push(-3);
console.log(stack.getMin()); // return -3
stack.pop();
console.log(stack.top());    // return 0
console.log(stack.getMin()); // return -2

