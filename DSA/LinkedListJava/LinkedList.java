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
            Node currNode = head;
            while (currNode.next != null) {
                currNode = currNode.next;
            }

            currNode.next = new_node;
        }

    }

    public void deleteTail() {
        Node currNode = head;

        if (currNode == null || currNode.next == null) {
            currNode = null;
        }

        while (currNode.next.next != null) {
            currNode = currNode.next;
        }
        currNode.next = null;
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
