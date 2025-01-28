// function Human(name, age, height, id) {
//     return {
//         name: name,    
//         age: age,      
//         height: height, 
//         id: id         
//     };
// }

// const human1 = Human("example_name", 25, 165, 101);
// const human2 = Human("example_name", 30, 175, 102);
// const human3 = Human("example_name", 22, 180, 103);


// console.log(human1);
// console.log(human2);
// console.log(human3);


function Car(name, year, engine, horsepower, color, owner) {
    return {
        name: name,               
        year: year,              
        engine: engine,          
        horsepower: horsepower,  
        color: color,             
        owner: owner              
    };
}

const car1 = Car("Tesla Model S", 2023, "Electric", 670, "Red", "example_name");
const car2 = Car("BMW", 2020, "V8", 450, "Blue", "example_name");
const car3 = Car("Mercedes", 2019, "V8", 121, "White", "example_name");

console.log(car1);
console.log(car2);
console.log(car3);

