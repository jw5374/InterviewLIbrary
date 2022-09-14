import java.util.Deque;
import java.util.LinkedList;

// Process the array D in the order of queries given in Q
// query 1: dequeue 2 elements then enqueue the average, if there is only one element simply dequeue it and enqueue it
// query 2: dequeue an element
// query 3: print the first element in the queue

// if queue is empty either do nothing, or if printing, print -1
public class ProcessArrayQueries {
    public static void processQueries(int N,int M,int[] D,int[] Q)
    {
      Deque<Integer> queue = new LinkedList<>();
      for(int i : D) {
        queue.addLast(i);
      }
      for(int i : Q) {
        switch(i) {
          case 1:
            if(queue.size() > 0) {
              if(queue.size() == 1) {
                break;
              }
              int a = queue.removeFirst();
              int b = queue.removeFirst();
              queue.addLast((a+b)/2);
            }
            break;
          case 2:
            if(queue.size() > 0) {
              queue.removeFirst();
            }
            break;
          case 3:
            if(queue.size() > 0) {
              System.out.print(queue.getFirst() + " ");
            } else {
              System.out.print(-1 + " ");
            }
            break;
        }
      }
    }
}
