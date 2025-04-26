console.log('beginning');

// Array
let pessoas = ['Gabriel', 'Lucas', 'Rafaela'];
console.log(pessoas[2]);

// Objeto
let pessoa = {
	nome: 'Bruno',
	idade: 25,
	cidade: 'Porto Alegre',
	amigos: pessoas,
};
console.log(`O ${pessoa.nome} tem ${pessoa.idade} anos, mora em ${pessoa.cidade} e tem ${pessoa.amigos.length} amigos, o nome dos amigos do Bruno são ${pessoa.amigos}`);

// Manipulando DOM
let para1 = document.querySelector('#para1');
para1.addEventListener('click', trocaTexto);
function trocaTexto() {
	para1.innerHTML = 'Calling the function';
};

let para2 = document.querySelector('#para2');
para2.addEventListener('click', () => {
	return para2.innerHTML = 'Calling the arrow function';
});

// Button manipulation
const btn = document.querySelector('.btn')
btn.style.background = 'blue';
if(btn.style.background !== 'red') {
	btn.addEventListener('mouseover', () => {
		btn.style.background = 'green';
	})
	btn.addEventListener('mouseout', () => {
		btn.style.background = 'blue';
	})
};
btn.addEventListener('click', () => {
	btn.style.background = 'red';
	btn.innerHTML = 'quebrei';
});