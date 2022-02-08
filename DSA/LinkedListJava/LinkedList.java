package DSA.LinkedListJava;

public class LinkedList {
    Node head;

    public void insertAtHead(int data) {
        Node new_node = new Node(data);
        new_node.next = null;

        new_node.next = head;
        head = new_node;
    }

    public void insertAtTail(int data) {
        // Create a new node with given data
        Node new_node = new Node(data);
        new_node.next = null;

        if (head == null) {
            head = new_node;
        } else {
            Node last = head;
            while (last.next != null) {
                last = last.next;
            }

            last.next = new_node;
        }

    }

    public void printList() {
        Node currNode = head;

        System.out.println("LinkedList: ");

        while (currNode != null) {
            System.out.println(currNode.data + " ");
            currNode = currNode.next;
        }
    }
}
