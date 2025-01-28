// class Bank {
//     constructor(owner, amount) {
//       this.owner = owner; 
//       this.amount = amount; 
//     }
  
//     deposit(amount) {
//       this.amount += amount; 
//     }
  
//     withdraw(amount) {
//       if (amount <= this.amount) { 
//         this.amount -= amount; 
//       } else {
//         console.log("not enough money"); 
//       }
//     }
  
//     show() {
//       console.log(this.owner + this.amount); 
//     }
//   }
  



constructor(name, type, color) {
    this.name = name;  
    this.type = type;   
    this.color = color; 
}
  
describe() {
     return `This is a ${this.color} ${this.type} named ${this.name}.`;
}
  
  
  