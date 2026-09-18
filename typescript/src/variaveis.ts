const numero: number = 10;
const nome: string = "Felipe";
const idade: number = 23;
const casado: boolean = false;

console.log("Numero:", numero);
console.log("Nome:", nome);
console.log("Idade:", idade);
console.log("Casado:", casado);

if (idade >= 18) {
  console.log(`A pessoa ${nome} e maior de idade.`);
} else {
  console.log(`A pessoa ${nome} e menor de idade.`);
}

if (casado) {
  console.log(`${nome} e casado.`);
} else {
  console.log(`${nome} nao e casado.`);
}

