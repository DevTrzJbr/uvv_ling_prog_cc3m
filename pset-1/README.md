# PSET1 - Algoritmo de Luhn

> "O algoritmo de Luhn foi desenvolvido por Hans Peter Luhn, da IBM, em 1954. Ele é capaz de detectar um erro simples em um dígito, assim como a maioria das transposições de um dígito com os dígitos adjacentes." - Inf UFRGS

[Problem Set 1 - credito](https://github.com/DevTrzJbr/uvv_ling_prog_cc3m/blob/main/pset-1/credito.pdf)

Este projeto consiste em validar cartões de crédito seguindo o critério de validação do algoritmo de Luhn e também descobrindo a bandeira a qual o cartão pertence; 

Podendo retornar:


| N° cartão             | Retorno      | Bandeira do cartão         |
| :-------------------- | :----------- | :------------------------- |
| `5233 4302 2696 0109` | `MASTERCARD` | MasterCard                 |
| `4884 8720 6116 1795` | `VISA`       | Visa                       |
| `3794 981464 72096`   | `AMEX`       | American Express           |
| `5048 3666 1159 6378` | `INVALIDO`   | Bandeira Invalida          |



