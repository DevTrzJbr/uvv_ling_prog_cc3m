# PSET2 - Filtragem de imagem por meio de transformações por pixel

[Estudo do problema](https://www.notion.so/jvbook/pset2-24ccee7bc3cb4c9492f1c2783871be5c)


## Questões do PSET
### Questão 1 - se você passar essa imagem pelo filtro de inversão, qual seria o output esperado?

O esperado ao passar uma imagem no filtro de inverção é que os pixels da imagem invertão, onde o branco fique preto e o preto fique branco.

![xadrêz](https://github.com/DevTrzJbr/uvv_ling_prog_cc3m/blob/main/pset-2/my_tests/chess.png)
![xadrêz invertido](https://github.com/DevTrzJbr/uvv_ling_prog_cc3m/blob/main/pset-2/my_tests/chess_inv.png)

## Questão 2

Execute seu filtro de inversão na imagem imagens_teste/peixe.png, salve o resultado como uma imagem PNG
e salve a imagem em seu repositório GitHub.

![peixe invertido](https://github.com/DevTrzJbr/uvv_ling_prog_cc3m/blob/main/pset-2/my_tests/fish_inv.png)

## Questão 3

Demonstre a etapa de correlação para o kernel 

| 0.00|-0.07| 0.00|
|-|-|-|
|-0.45|1.20| -0.25|
|0.00|-0.12| 0.00|

Onde os pixels são 

| 80|53|99|
|-|-|-|
|129|**127**|148|
|175|174|193|

Qual será o valor do pixel na imagem de saída no meio da matriz de pixel?

 - Multiplicar cada valor de pixel pelo valor associado do kernel e soma-los
 
 - resultado = (0.00 * 80) + (-0.07 * 53) + (0.00 * 99) +
 (-0.45 * 129) + (1.20 * 127) + (-0.25 * 148) +
 (0.00 * 175) + (-0.12 * 174) + (0.00 * 193)
 
 - resultado = 0 + (-3.71) + 0 + (-58.05) + 152.4 + (-37) + 0 + 0 + (-20.88) + 0

- **resultado = 32.76**

## Questão 4

Quando você tiver implementado seu código, tente executá-lo em imagens_teste/porco.png com o seguinte kernel 9 × 9:

|0 |0 |0 |0 |0 |0 |0 |0 |0|
|-|-|-|-|-|-|-|-|-|
|0 |0 |0 |0 |0 |0 |0 |0 |0|
|1 |0 |0 |0 |0 |0 |0 |0 |0|
|0 |0 |0 |0 |0 |0 |0 |0 |0|
|0 |0 |0 |0 |0 |0 |0 |0 |0|
|0 |0 |0 |0 |0 |0 |0 |0 |0|
|0 |0 |0 |0 |0 |0 |0 |0 |0|
|0 |0 |0 |0 |0 |0 |0 |0 |0|
|0 |0 |0 |0 |0 |0 |0 |0 |0|

Ao rodar esse kernel, salve a imagem resultante em seu repositório GitHub.

![porco](https://github.com/DevTrzJbr/uvv_ling_prog_cc3m/blob/main/pset-2/my_tests/pig.png)
![porco correlacionado](https://github.com/DevTrzJbr/uvv_ling_prog_cc3m/blob/main/pset-2/my_tests/pig_correlated.png)

Porco &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Porco correlacionado

## Questão 5 

Se quisermos usar uma versão desfocada B que foi feita com um kernel de desfoque de caixa de 3 × 3, que kernel k poderíamos usar para calcular toda a imagem nítida com uma única correlação?

Execute seu filtro de nitidez na imagem imagens_teste/python.png usando um kernel de tamanho 11

![python](https://github.com/DevTrzJbr/uvv_ling_prog_cc3m/blob/main/pset-2/my_tests/python.png)
![python nítido](https://github.com/DevTrzJbr/uvv_ling_prog_cc3m/blob/main/pset-2/my_tests/python_sharpened.png)

Python &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Python nítido
