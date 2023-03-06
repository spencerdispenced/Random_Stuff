package BasicDSA.DS.LinkedListJava;

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

        // Remove Head if only one node in list
        if (head == null || head.next == null) {
            head = null;
            return;
        }

        while (currNode.next.next != null) {
            currNode = currNode.next;
        }
        currNode.next = null;
    }

    public void deleteNode(int target_data) {
        Node currNode = head;

        if (head.data == target_data) {
            head = head.next;
            return;
        }

        while (currNode.next.data != target_data) {
            currNode = currNode.next;
        }

        currNode.next = currNode.next.next;
    }

    public void printList() {
        Node currNode = head;

        String output = "LinkedList: ";

        while (currNode != null) {
            output += currNode.data + " -> ";
            currNode = currNode.next;
        }

        System.out.println(output);
    }
}
