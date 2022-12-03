


const binarySearch = (arr, n) => {
    let low = 0;
    let high = arr.length - 1;
    let mid = 0;

    while (low <= high) {
        mid = Math.floor((low + high) / 2);
        if (n < arr[mid]) {
            high = mid - 1;
        }
        else if (n > arr[mid]) {
            low = mid + 1;
        }
        else {
            return true;
        }
    }
    return false;
}


const testArr = [1, 3, 6, 8, 9, 10];

console.log(binarySearch(testArr, 6));
console.log(binarySearch(testArr, 5));