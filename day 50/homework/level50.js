
// function addMatrices(matrix1, matrix2) {
//     if (matrix1.length !== matrix2.length || matrix1[0].length !== matrix2[0].length) {
//         throw new Error("error.");
//     }
//     let result = [];
//     for (let i = 0; i < matrix1.length; i++) {
//         let row = []; 
//         for (let j = 0; j < matrix1[i].length; j++) {
//             row.push(matrix1[i][j] + matrix2[i][j]);
//         }
//         result.push(row);
//     }
//     return result;
// }




// function transposeMatrix(matrix) {
//     let result = [];
//     for (let j = 0; j < matrix[0].length; j++) {
//         let row = [];
//         for (let i = 0; i < matrix.length; i++) {
//             row.push(matrix[i][j]); 
//         }
//         result.push(row);
//     }
//     return result;
// }



// function sumDiagonals(matrix) {
//     let mainDiagonalSum = 0;  
//     let secondaryDiagonalSum = 0;  
//     let n = matrix.length;  

//     for (let i = 0; i < n; i++) {
//         mainDiagonalSum += matrix[i][i]; 
//         secondaryDiagonalSum += matrix[i][n - i - 1]; 
//     }

//     return [mainDiagonalSum, secondaryDiagonalSum];
// }


