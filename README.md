# Laboratorios de programacao - faculdade

Este repositorio reune laboratorios realizados em sala de aula na faculdade.
O material faz parte do meu processo de ensino, aprendizagem e desenvolvimento
em programacao, portanto registra exercicios introdutorios, testes e a evolucao
dos conceitos estudados.

Os exemplos abordam Python, programacao orientada a objetos, JavaScript e
TypeScript. Os arquivos foram organizados e revisados para corrigir pequenos
problemas de tipos, interpolacao de texto e convencoes de nomes, mantendo o
objetivo didatico de cada atividade.

> Projeto educacional em desenvolvimento. Os exemplos representam praticas de
> sala de aula e podem ser ampliados conforme o avancar da disciplina.

## Estrutura

```text
exercicios-faculdade/
|-- python/
|   |-- listas/
|   |   `-- lista.py
|   `-- poo/
|       |-- aluno.py
|       `-- cachorro.py
|-- typescript/
|   |-- src/
|   |   |-- app.ts
|   |   |-- variaveis.ts
|   |   `-- soma.js
|   |-- package.json
|   `-- tsconfig.json
`-- README.md
```

## Executar tudo no Windows

De dois cliques em `executar-exemplos.bat` para verificar e executar todos os
exercicios em sequencia. A janela permanece aberta para que os resultados
possam ser lidos.

## Python: listas

O exemplo apresenta listas vazias, listas tipadas, listas com diferentes tipos,
geracao de numeros pares e acesso por indices positivos e negativos.

```powershell
python python/listas/lista.py
```

## Python: orientacao a objetos

`aluno.py` demonstra atributos, metodos, validacao de notas, calculo de media e
estado de aprovacao. `cachorro.py` mostra que dois objetos criados pela mesma
classe continuam sendo instancias diferentes.

```powershell
python python/poo/aluno.py
python python/poo/cachorro.py
```

## TypeScript

Entre na pasta `typescript`, instale as dependencias e execute os exemplos:

```powershell
cd typescript
npm install
npm run verificar
npm run soma
npm run variaveis
npm run javascript
```

## Principais correcoes estudadas

- Uso de colchetes para criar uma lista em Python.
- Separacao correta dos itens de uma lista com virgulas.
- Classes Python nomeadas com inicial maiuscula.
- Mensagens de validacao coerentes com a regra aplicada.
- Interpolacao TypeScript usando crases e `${nome}`.
- Diferenca entre soma numerica e concatenacao de texto no JavaScript.

## Objetivo do repositorio

- Registrar minha evolucao durante as aulas.
- Praticar os fundamentos das linguagens estudadas.
- Comparar problemas encontrados com suas respectivas correcoes.
- Manter os laboratorios organizados para consulta e continuidade dos estudos.
