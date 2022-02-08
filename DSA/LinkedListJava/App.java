package DSA.LinkedListJava;

public class App {
    public static void main(String[] args) {
        LinkedList ll = new LinkedList();

        ll.insertAtTail(5);
        ll.insertAtTail(1);
        ll.insertAtTail(7);
        ll.insertAtTail(5);

        ll.insertAtHead(1);
        ll.insertAtHead(1);
        ll.insertAtHead(3);
        ll.insertAtTail(8);
        ll.deleteTail();

        ll.printList();
    }
}