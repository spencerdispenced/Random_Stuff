package BasicDSA.DS.LinkedListJava;

public class App {
    public static void main(String[] args) {
        LinkedList ll = new LinkedList();

        ll.insertAtTail(5);
        ll.insertAtTail(1);
        ll.insertAtTail(6);
        ll.insertAtHead(1);
        ll.insertAtHead(1);
        ll.insertAtHead(3);
        ll.insertAtTail(8);

        ll.printList();

        ll.deleteNode(6);
        ll.printList();
        ll.deleteNode(8);

        ll.printList();

    }
}