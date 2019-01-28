function bubble_sort(arr) {
    let j, temp, flag;
    for(let i = arr.length; i > 0 ; i--) {
        flag = true;
        for(j=1; j <= i-1 ; j++) {
            if (arr[j] < arr[j-1]) {
                temp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = temp;
                flag = false; 
            }
        }
        console.log('Pass: ', arr);
        if (flag) {
            break;
        }
    }
    return arr;
}

arr = [ 2, 3, 1, 4];
console.log('Input: ', arr);
console.log('Sorted array: ', bubble_sort(arr));
arr = [ 1, 2, 3, 4];
console.log('Input: ', arr);
console.log('Sorted array: ', bubble_sort(arr));
arr = [ 4, 3, 2, 1];
console.log('Input: ', arr);
console.log('Sorted array: ', bubble_sort(arr));