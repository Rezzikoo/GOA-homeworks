function Car(brand, model, year) {
    return {
        brand: brand,
        model: model,
        year: year
    };
}

const car1 = Car("Toyota", "Corolla", 2020);
const car2 = Car("Tesla", "Model 3", 2023);
const car3 = Car("Mercedes", "G-wagon", 2019);

function Animal(type, name, age) {
    return {
        type: type,
        name: name,
        age: age
    };
}

const animal1 = Animal("Dog", "example_name", 4);
const animal2 = Animal("Cat", "example_name", 2);
const animal3 = Animal("Hamster", "example_name", 3);

function Student(name, grade, school) {
    return {
        name: name,
        grade: grade,
        school: school
    };
}

const student1 = Student("example_name", "9", "example_school");
const student2 = Student("example_name", "12", "example_schoo");
const student3 = Student("example_name", "7", "example_schoo");

console.log(car1, car2, car3);
console.log(animal1, animal2, animal3);
console.log(student1, student2, student3);
