
function sumRowsAndColumns(matrix) {
    let rowSums = [];  
    let colSums = Array(matrix[0].length).fill(0); 
    for (let i = 0; i < matrix.length; i++) {
        let rowSum = 0;
        for (let j = 0; j < matrix[i].length; j++) {
            rowSum += matrix[i][j];  
            colSums[j] += matrix[i][j];  
        }
        rowSums.push(rowSum);  
    }
    return [rowSums, colSums];
}