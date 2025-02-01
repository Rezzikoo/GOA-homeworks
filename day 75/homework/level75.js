// function Car(brand, model, year, engine) {
//     this.brand = brand;
//     this.model = model;
//     this.year = year;
//     this.engine = engine;

//     this.getDescription = function() {
//         return this.brand + " " + this.model + ", " + this.year + ", " + this.engine + "L";
//     };
// }



// function Book(title, author, pages, year) {
//     this.title = title;
//     this.author = author;
//     this.pages = pages;
//     this.year = year;

//     this.pagesPerDay = function() {
//         return this.pages / 7;
//     };
// }



function Athlete(name, age, sport, Hours) {
    this.name = name;
    this.age = age;
    this.sport = sport;
    this.Hours = Hours;

    this.increaseTraining = function() {
        return this.Hours * 0.2; 
    };
}





