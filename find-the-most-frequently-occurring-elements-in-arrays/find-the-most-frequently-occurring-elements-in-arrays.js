function getMostFrequent(json) {
  return json.temperature.map(ls=>mode(ls))
}


function mode(arr) {
  const counts = {};
  let maxCount = 0;
  let maxKey;
  for (let i = 0; i < arr.length; i++) {
    const key = arr[i];
    const count = (counts[key] = (counts[key] || 0) + 1);
    if (count >= maxCount) {
      maxCount = count;
      maxKey = key;
    }
  }
  return maxKey;
}