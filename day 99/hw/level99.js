function mostFrequentItemCount(arr) {
    if (arr.length === 0) return 0;
  
    let counts = {};
    let maxCount = 0;
  
    for (let i = 0; i < arr.length; i++) {
      let item = arr[i];
      if (counts[item]) {
        counts[item]++;
      } else {
        counts[item] = 1;
      }
  
      if (counts[item] > maxCount) {
        maxCount = counts[item];
      }
    }
  
    return maxCount;
  }
  