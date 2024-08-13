# Projeto `Algorithms`

## Entregáveis

<details>
  <summary><strong>O que foi desenvolvido</strong></summary>

- O projeto traz o desafio de otimizar algoritmos desenvolvendo a capacidade de implementar soluções diferentes para diversos problemas do dia a dia!
  
- Habilidades desenvolvidas:
  - Lógica de programação;
  - Capacidade de interpretação de problemas;
  - Capacidade de interpretação de um código legado;
  - Capacidade de otimizar a resolução de problemas;
  - Otimização de algoritmos.

</details>

## Requisitos

### Algoritmo de busca para encontrar o número de alunos estudando no mesmo horário

- O algoritmo utiliza uma solução iterativa;
- Retorna a quantidade de estudantes presentes para uma entrada específica;
- Retorna `None` se em `permanence_period` houver alguma entrada inválida;
- Retorna `None` se  `target_time` receber um valor vazio;
- A função se comporta, por meio de análise empírica, como no máximo O(n), ou seja, com complexidade assintótica linear.

### Criptografia de inversões

- Recebe uma string `message` e um inteiro `key` como parâmetros;
- Se `key` e `message` não possuírem os tipos corretos, é lançado uma exceção;
- Se `key` não for um índice positivo válido de `message`, retorna a string `message` invertida
- Se `key` for ímpar:
  - divide `message` no índice `key`, inverte os caracteres de cada parte, e retorna a união das partes novamente com `"_"` entre elas.
- Se `key` for par:
  - divide `message` no índice `key`, inverte a posição das partes, inverte os caracteres de cada parte, e retorna a união das partes novamente com `"_"` entre elas.

### Palíndromos recursivo

- A função determina se uma palavra é um palíndromo ou não;
- Recebe uma string de parâmetro e retorna um _booleano_;
- O algoritmo foi desenvolvido utilizando uma solução recursiva.

### Palíndromos (Iteratividade)

- A função determina se uma palavra é um palíndromo ou não;
- O algoritmo utiliza a solução iterativa;
- O algoritmo foi construído para atingir a complexidade `O(n)`.

### Anagramas (Algoritmo de ordenação)

- O algoritmo compara duas _strings_, ordena e identifica se uma é um anagrama da outra;
- A função recebe duas strings de parâmetro e o retorno é uma tupla `()` com a primeira string ordenada, a segunda string ordenada e um _booleano_, representando se são anagramas ou não;
- O algoritmo foi construído para atingir a complexidade `O(n log n)`.

### Números repetidos (Algoritmo de busca)

- Retorna apenas o número duplicado da lista.
- O algoritmo foi construído para atingir a complexidade `O(n log n)`.
