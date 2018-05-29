function SelectionSortAscending(array) {
  for (let pIndex = 0; pIndex < array.length - 1; pIndex++) {
    let minIndex = pIndex
    for (let cIndex = pIndex + 1; cIndex < array.length; cIndex++) {
      if (array[minIndex] > array[cIndex]) {
          minIndex = cIndex;
      }
    }
    let temp = array[pIndex];
    array[pIndex] = array[minIndex];
    array[minIndex] = temp;
  }
  return array;
}

function SelectionSortDescending(array){
  for (let pIndex = 0; pIndex < array.length - 1; pIndex++) {
    let maxIndex = pIndex
    for (let cIndex = pIndex + 1; cIndex < array.length; cIndex++) {
      if (array[maxIndex] < array[cIndex]) {
        maxIndex = cIndex;
      }
    }
    let temp = array[pIndex];
    array[pIndex] = array[minIndex];
    array[minIndex] = temp;
  }
  return array;
}