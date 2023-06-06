


const binarySearch = (nums, target) => {
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);

        if (nums[mid] > target)
            right = mid - 1;

        else if (nums[mid] < target)
            left = mid + 1;

        else 
            return mid;
        
    }
    return -1;
}


const nums1 = [-1, 0, 3, 5, 9, 12];
const target1 = 9;

const nums2 = [-1, 0, 3, 5, 9, 12];
const target2 = 2;

const nums3 = [1, 3, 6, 8, 9, 10];
const target3 = 6;
const target4 = 5;

console.log(binarySearch(nums1, target1))  // 4
console.log(binarySearch(nums2, target2))  // -1
console.log(binarySearch(nums3, target3))  // 2
console.log(binarySearch(nums3, target4))  // -1