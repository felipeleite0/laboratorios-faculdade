"use strict";

const soma = (a, b) => {
  return a + b;
};

console.log("Soma de numeros:", soma(4, 5));
console.log("Concatenacao de texto e numero:", soma("43", 5));
console.log("Conversao seguida de soma:", soma(Number("43"), 5));

