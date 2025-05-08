function nameToMatrix(name) {
  if (name.length === 0) return "name must be at least one letter";

  
  let size = 1;
  while (size * size < name.length) {
    size++;
  }

  
  while (name.length < size * size) {
    name += '.';
  }

 
  const result = [];
  let index = 0;

  for (let i = 0; i < size; i++) {
    const row = [];
    for (let j = 0; j < size; j++) {
      row.push(name[index]);
      index++;
    }
    result.push(row);
  }

  return result;
}
