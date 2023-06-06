package BasicDSA.Algo.Sorting.MergeSort;

public class MergeSort {

    public static void sort(int[] intArr, int start, int end ) {
        if (end <= start)
            return;

        int mid = (start + end) / 2;
        sort(intArr, start, mid);
        sort(intArr, mid+1, end);
        merge(intArr, start, mid, end);
    }

    public static void merge(int[] intArr, int start, int mid, int end) {
        int tempArr[] = new int [end - start + 1];

        // Index conter for left and right side of array
        int leftSlot = start;
        int rightSlot = mid + 1;
        int k = 0;

        while (leftSlot <= mid && rightSlot <= end) {
            if (intArr[leftSlot] < intArr[rightSlot]) {
                tempArr[k] = intArr[leftSlot];
                leftSlot++;
            } else {
                tempArr[k] = intArr[rightSlot];
                rightSlot++;
            }
            k++;
        }

        if (leftSlot <= mid) {
            while (leftSlot <= mid) {
                tempArr[k] = intArr[leftSlot];
                leftSlot++;
                k++;
            }
        } else if (rightSlot <= end) {
            while (rightSlot <= end) {
                tempArr[k] = intArr[rightSlot];
                rightSlot++;
                k++;
            }
        }

        for (int i = 0; i < tempArr.length; i++) {
            intArr[start + 1] = tempArr[i];
        }
    }
    
    public static void main(String[] args) {
        int[] inputArr = {9, 7, 3, 1, 6, 3, 2, 6, 8, 9, 2, 3, 0};
        

        for (int i = 0; i < inputArr.length; i++) {
            System.out.print(inputArr[i] + " ");
        }

        sort(inputArr, 0, inputArr.length-1);

        System.out.println();

        for (int i = 0; i < inputArr.length; i++) {
            System.out.print(inputArr[i] + " ");
        }
    }
}
