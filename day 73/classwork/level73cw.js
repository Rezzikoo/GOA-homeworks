// let car = {
//     maker: "BMW",
//     model: "E 39",
//     color: "Red",
//   };
//   console.log(car.model);



// let example = {
//     row_0: [2, 4, 6, 8, 10], 
//     row_1: [1, 3, 5, 7, 9]   
//   };
// for (let i = 0; i < example.row_0.length; i++) {
//     console.log(example.row_0[i], example.row_1[i]);
//   }
  


function example(obj) {
    let { quantity, element } = obj;
    let result = [];
    
    for (let i = 0; i < quantity; i++) {
      result.push(element);
    }
  
    return result;
  }
  
  
  
  