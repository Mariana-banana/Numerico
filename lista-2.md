-----
Dúvidas e tarefas:

Interpolação e ajuste
2. O que é diferenças finitas e como usar?
3. lagrange? - n-1
4. Função correta para encontrar melhor aproximação (analise - gica)

5. Passar funções de ajuste a limpo e funcao de interpolação

--
Derivadas e Integrais

--
EDO's e PVI's

-----

------------------------------------------------------------------
Lista 2 - Cálculo Numérico
------------------------------------------------------------------

* Ajuste de Curvas = muitos pontos
* Interpolação = poucos pontos

1. Encontre a parábola que melhor se ajusta aos pontos (−3; 3), (0; 1), (2; 1) e (4; 3).

Por ajuste de curvas
```scilab

x = [-3; 0; 2; 4];
y = [3; 1; 1; 3];
X = [x.^2, x, ones(x)];
coeffs = X \ y; // resolucao do sistema linear
a = coeffs(1);
b = coeffs(2);
c = coeffs(3);
printf("y = (%.4f)x^2 + (%.4f)x + (%.4f)\n\n", a, b, c);

```
> => y = (0.1785)x^2 + (-0.1925)x + (0.8505)

por min quadraticos:
```scilab
function coefs = ajuste_parabola(X, Y)
    X = X(:); 
    Y = Y(:);
    n = length(X);
    M = [ones(n, 1), X, X.^2];
    A = M' * M;
    B = M' * Y;
    coefs = A \ B;
endfunction

x = [-3, 0, 2, 4];
y = [3, 1, 1, 3];
c = ajuste_parabola(x, y);
printf("y = (%.4f)x^2 + (%.4f)x + (%.4f)\n", c(3), c(2), c(1));
```

para reta:
```scilab
x = [0; 1; 2; 3; 4];
y = [0; 1; 2; 4; 5];
X = [x, ones(x)];
coeffs = X \ y; // resolucao do sistema linear
a = coeffs(1);
b = coeffs(2);
printf("y = (%.4f)x + (%.4f)\n\n", a, b);

```

--------------------------------------------------------------------------------------
2. Encontre a função exponencial que melhor se ajusta aos pontos 
(0; 1, 5), (1; 2, 5), (2; 3, 5), (3; 5) e (4; 7, 5).

```scilab
x = [0; 1; 2; 3; 4];
y = [1.5; 2.5; 3.5; 5; 7.5];

if any(y <= 0) then
    error("Este método de linearização requer que todos os valores de y sejam positivos.");
end

Y = log(y); 
X = [x, ones(x)];

// Resolução do sistema linearizado com mínimos quadrados
// O resultado será o vetor de coeficientes [a; B]
coeffs_linear = X \ Y;

a = coeffs_linear(1);
B = coeffs_linear(2);
c = exp(B);
printf("y = (%.4f) * e^(%.4fx)\n\n", c, a);

```

> => y = (1.5799) * e^(0.3912x)

Versão 2
```scilab
function [a, c] = ajuste_exponencial_mq(X, Y_original)
    X = X(:);
    Y_original = Y_original(:);
    disp(Y_original)
    
    if or(Y_original <= 0) then
        error("Requer que todos os valores de Y sejam positivos.");
    end
    
    Y_linear = log(Y_original);
    n = length(X);
    M = [ones(n, 1), X];
    coefs_linear = (M' * M) \ (M' * Y_linear);
    B = coefs_linear(1);
    A = coefs_linear(2);
    c = exp(B);
    printf("y = (%.4f) * e^(%.4fx)\n\n", c, a);
endfunction

// Usando os pontos do exemplo da outra pergunta:
x = [0; 1; 2; 3; 4];
y = [1.5; 2.5; 3.5; 5; 7.5];
ajuste_exponencial_mq(x, y);
```

--------------------------------------------------------------------------------------
3. Sabendo que a intensidade do campo elétrico no ar, de um ponto em relação a uma carga puntiforme de 650 Coulomb, varia com a distância em cm de acordo com a tabela:

X    | Y
---- | ----
5    | 26
7.5  | 11.56
10   | 6.50
12.5 | 4.16
15   | 2.88

Calcule a intensidade do campo elétrico em um ponto situado a 8.5cm da carga.
Com polinomio de lagrange é possível calcular o polinomio de grau n-1.

```scilab
function P = lagrange(X, Y, point)
    n = length(X); // Número de pontos
    P = 0; // Inicializa o polinômio interpolador
    
    for i = 1:n
        Li = 1; // Inicializa o polinômio de Lagrange L_i(x) como 1
        
        for j = 1:n
            if i ~= j then
                Li = Li * (poly(X(j), 'x') / (X(i) - X(j)));
            end
        end
        
        P = P + Y(i) * Li;
    end
    disp(horner(P, point))
endfunction

x = [5; 7.5; 10; 12.5; 15];
y = [26; 11.56; 6.5; 4.16; 2.88];

lagrange(x, y, 8.5)
```

> => 8.8953600
> => 134.66 -39.533333x +4.7154667x^2 -0.2577067x^3 +0.0053333x^4

--------------------------------------------------------------------------------------
4. O calor especı́fico (c) da água em função da temperatura em o C é:

X   | Y
--- | --------
30  | 0,99826
35  | 0,99818
40  | 0,99828

Calcule o calor especı́fico para T = 37.5 C.

```scilab
x = [30; 35; 40];
y = [0.99826; 0.99818; 0.99828];
lagrange(x, y, 37.5)
```

- Por Lagrange
> => 0.9982075
> => 1.00252 -0.00025x +0.0000036x^2

### Função potência
```scilab
function [a, b] = ajuste_potencia(X_dados, Y_dados)
    // Garante que os vetores de entrada estejam no formato de coluna
    X_dados = X_dados(:);
    Y_dados = Y_dados(:);
    
    if or(X_dados <= 0) | or(Y_dados <= 0) then
        error("Ajuste de potência por linearização requer que todos os valores de X e Y sejam positivos.");
    end
    
    // --- Etapa 2: Linearizar os dados aplicando o logaritmo ---
    X_log = log(X_dados);
    Y_log = log(Y_dados);
    
    // --- Etapa 3: Fazer um ajuste de RETA nos dados linearizados ---
    // O modelo linear é: Y_log = ln(a) + b * X_log
    // Montamos a matriz M para o sistema M*p = Y_log, onde p = [ln(a); b]
    n = length(X_log);
    M = [ones(n, 1), X_log]; 
    coefs_lineares = M \ Y_log;
    coef_linear_B = coefs_lineares(1); 
    coef_angular_m = coefs_lineares(2); 
    
    b = coef_angular_m;
    a = exp(coef_linear_B);
    printf("y = (%.8f) * x^(%.8f)\n", a, b);
endfunction

x = [1,   2,   3,    4,    5,    6];
y = [2.1, 5.8, 10.5, 16.2, 22.5, 29.5];
ajuste_potencia(x, y);
```

--------------------------------------------------------------------------------------
5. Dada a tabela
x  | f(x)
-- | -----
-2 | -7
-1 | 0
0  | 1
1  | α
2  | 9
3  | 28

determine f(1).

```scilab
x = [-2; -1; 0; 2; 3];
y = [-7; 0; 1; 9; 28];
lagrange(x, y, 1)
```

> => 2.0000000
> => 1 -4.441D-16x^2 +1x^3

--------------------------------------------------------------------------------------
6. Determina-se o alongamento de uma mola em (mm) em função da carga P (kgf) que sobre
ela atua, obtendo-se:
x   | P
--- | ---
10  | 105
15  | 172
20  | 253
25  | 352
30  | 473
35  | 619

Interpolando adequadamente por meio de polinômios de 3o grau, encontre as cargas que
produzem os seguintes alongamentos na mola:

```scilab
x = [10; 15; 20; 25; 30; 35];
y = [105; 172; 253; 352; 473; 619];
lagrange(x, y, 12)
```

> =>   3 +8.1266667x +0.2333333x^2 -0.005x^3 +0.0002667x^4 -0.0000027x^5
> => f(12) = 130.34605
> => f(22) = 290.20525
> => f(31) = 500.13286

- Interpolação polinomial simples

```scilab
function y = inter_poli(n,X,Y)
    A = zeros(length(X), n);
    B = Y;

    // Preenche a matriz A com as potências de X
    for i = 0:n-1
        A(:, i+1) = X .^i;
    end
    y = inv(A)*B
endfunction

x = [10; 15; 20; 25; 30; 35];
y = [105; 172; 253; 352; 473; 619];
function y_alvo = inter_poli_eval(X, Y, t_alvo)
    X = X(:);
    Y = Y(:);
    n = length(X);
    A = zeros(n, n); // Matriz de Vandermonde
    for i = 0:n-1
        A(:, i+1) = X .^ i;
    end
    coefs = A \ Y;
    P = poly(coefs, 'x', 'coeff');
    disp(P);
    y_alvo = horner(P, t_alvo);
    disp(y_alvo);
endfunction

inter_poli_eval(x, y, 12);
```

> => 3 +8.1266667x +0.2333333x^2 -0.005x^3 +0.0002667x^4 -0.0000027x^5

--------------------------------------------------------------------------------------
7. Considere a variação da temperatura de ebulição da água em função da pressão 
barométrica dada por:
P    | T (o C)
700  | 97,71
710  | 98,11
720  | 98,49
730  | 98,88
740  | 99,26
780  | 100,73

Achar a função que melhor representa os dados da tabela.

```scilab
P = [700, 710, 720, 730, 740, 780];
T = [97.71, 98.11, 98.49, 98.88, 99.26, 100.73];

p_linear = polyfit(P, T, 1);
p_linear = poly(p_linear, 'x', 'coeff');
p_quad = polyfit(P, T, 2);
p_cub = polyfit(P, T, 3);
disp(p_linear);
disp(p_quad);
disp(p_cub);
```

```scilab
function melhor_modelo = analise(X, Y)
    
    // --- Reta ---
    buf_reta = diff(Y) ./ diff(X);
    cv_reta = stdev(buf_reta) / abs(mean(buf_reta));
    disp("Reta (diff Y / diff X):")
    disp(buf_reta)
    disp("CV Reta:")
    disp(cv_reta)
    
    // --- Parábola (usando diferenças quadráticas) ---
    buf_para = (diff(Y)).^2 ./ diff(X.^2);
    cv_para = stdev(buf_para) / abs(mean(buf_para));
    disp("Parábola (diff Y^2 / diff X^2):")
    disp(buf_para)
    disp("CV Parábola:")
    disp(cv_para)
    
    // --- Cúbica (usando diferenças cúbicas) ---
    buf_cub = (diff(Y)).^3 ./ diff(X.^3);
    cv_cub = stdev(buf_cub) / abs(mean(buf_cub));
    disp("Cúbica (diff Y^3 / diff X^3):")
    disp(buf_cub)
    disp("CV Cúbica:")
    disp(cv_cub)
    
    // --- Exponencial ---
    buf_exp = diff(log(Y)) ./ diff(X);
    cv_exp = stdev(buf_exp) / abs(mean(buf_exp));
    disp("Exponencial (diff ln(Y) / diff X):")
    disp(buf_exp)
    disp("CV Exponencial:")
    disp(cv_exp)
    
    // --- Potência ---
    buf_pot = diff(log(Y)) ./ diff(log(X));
    cv_pot = stdev(buf_pot) / abs(mean(buf_pot));
    disp("Potência (diff ln(Y) / diff ln(X)):")
    disp(buf_pot)
    disp("CV Potência:")
    disp(cv_pot)
    
    // Armazenar CVs para comparar
    cvs = [cv_reta, cv_para, cv_cub, cv_exp, cv_pot];
    modelos = ["Reta", "Parábola", "Cúbica", "Exponencial", "Potência"];
    
    // Encontrar índice do menor CV
    [min_cv, idx] = min(cvs);
    
    disp("Melhor modelo baseado no menor coeficiente de variação (CV): " + modelos(idx));
    
    // Plotar os pontos
    clf();
    plot(X, Y, 'go');
    xtitle("Análise dos dados");
    
    // Retornar o nome do melhor modelo
    melhor_modelo = modelos(idx);
endfunction

function best_p = analise_melhor_ajuste(P, T)
    P = P(:);
    T = T(:);
    n = length(P);
    
    // Ajuste linear (grau 1)
    M_linear = [ones(n,1), P];
    coef_linear = M_linear \ T;
    T_fit_linear = M_linear * coef_linear;
    erro_linear = mean((T - T_fit_linear).^2);
    p_linear = poly(coef_linear, 'P', 'coeff');

    // Ajuste quadrático (grau 2)
    M_quad = [ones(n,1), P, P.^2];
    coef_quad = M_quad \ T;
    T_fit_quad = M_quad * coef_quad;
    erro_quad = mean((T - T_fit_quad).^2);
    p_quad = poly(coef_quad, 'P', 'coeff');

    // Ajuste cúbico (grau 3)
    M_cub = [ones(n,1), P, P.^2, P.^3];
    coef_cub = M_cub \ T;
    T_fit_cub = M_cub * coef_cub;
    erro_cub = mean((T - T_fit_cub).^2);
    p_cub = poly(coef_cub, 'P', 'coeff');
    
    // Exibe os erros para análise
    printf("--- Análise dos Erros ---\n");
    printf("Erro do ajuste linear (grau 1):     %f\n", erro_linear);
    printf("Erro do ajuste quadrático (grau 2):  %f\n", erro_quad);
    printf("Erro do ajuste cúbico (grau 3):      %f\n\n", erro_cub);
    
    // Compara os erros e seleciona o melhor polinômio
    erros = [erro_linear, erro_quad, erro_cub];
    [min_erro, indice_melhor] = min(erros);
    
    select indice_melhor
    case 1
        best_p = p_linear;
        grau = 1;
    case 2
        best_p = p_quad;
        grau = 2;
    case 3
        best_p = p_cub;
        grau = 3;
    end
    printf("O melhor ajuste foi o polinômio de grau %d.\n", grau);
endfunction

x = [700, 710, 720, 730, 740, 780];
y = [97.71, 98.11, 98.49, 98.88, 99.26, 100.73];
disp(analise(x,y));
```

> => Função potência
> => y = (15.4949) * x^(0.2811)

--------------------------------------------------------------------------------------
8. Considere a relação entre a resistência à tração do aço e a variação da temperatura
conforme
T   | Tr (kg/cm2 )
250 | 5720
330 | 5260
412 | 4450
485 | 2780
617 | 1506

```scilab
x = [250; 330; 412; 485; 617];
y = [5720; 5260; 4450; 2780; 1506];

x = [250, 330, 412, 485, 617];
y = [5720, 5260, 4450, 2780, 1506];
analise(x,y);
analise_melhor_ajuste(x,y);
```

a) Determinar a função que melhor se ajusta a tabela de dados.

```
// por reta
x = [250, 330, 412, 485, 617]';
y = [5720, 5260, 4450, 2780, 1506]';
X = [x, ones(x)];
coeffs = X \ y; // resolucao do sistema linear
P = poly(coeffs, 'x', 'coeff');
disp(P);
a = coeffs(1);
b = coeffs(2);
printf("y = (%.4f)x + (%.4f)\n\n", a, b);

// por cubica
p_cub = polyfit(x, y, 3);
```

> => -6036.6085 +101.42201P -0.2683814P^2 +0.0002006P^3

b) Encontre a resistência à tração para T = 380o C e 730o C.

```
> => horner(p, 380)
> ans = 
>   4757.0934

> => horner(p, 730)
> ans = 
>   3019.8850
```

--------------------------------------------------------------------------------------
9. A tabela mostra a variação do coeficiente de atrito entre uma roda e um trilho seco
v(km/h) | µ
------- | ------
10      | 0,313
20      | 0,250
30      | 0,215
40      | 0,192
60      | 0,164
70      | 0,154

```scilab
x = [10,20,30,40,60,70]';
y = [0.313, 0.250, 0.215, 0.192, 0.164, 0.154];
analise(x,y);
ajuste_potencia(x,y)
0.7395 * 50^(-0.3668)
```

a) Determine o coeficiente de atrito quando a velocidade for 50 km/h.
> => 0.7395 * 50^(-0.3668)
>      0.1760986

b) Determine o coeficiente de atrito quando a velocidade for 120 km/h.
> => 0.7395 * 120^(-0.3668)
>      0.1277305

Extra.

Tabela 5.4: Dados a serem interpolados
x   | f (x)
0,1 | 4
0,2 | 16
0,3 | −4
0,4 | −16

```
x=[0.1;0.2;0.3;0.4];
y=[4;16;-4;-16];
inter_poli(4, x, y)
```
--------------------------------------------------------------------------------------
10. Calcule aproximações da segunda derivada de f (x) = cos(2x) em x = 0,7 com h = 0,1,
h = 0,01, h = 0,001. Utilize 4 casas decimais após a vı́rgula em seus cálculos. Compare
os resultados com o valor real f”(0,7) = −cos(1,4).

```
// Primeira derivada
deff('y = f(x)', 'y = cos(2*x)')  
x0 = 0.7
h  = 0.1
df = (f(x0 + h) - f(x0 - h)) / (2*h)

// Segunda derivada
disp(h^2)
d2f = (f(x0 + h) - 2*f(x0) + f(x0 - h)) / h^2

// terceira derivada
d3f = (f(x0 + 2*h) - 2*f(x0 + h) + 2*f(x0 - h) - f(x0 - 2*h)) / (2*h^3)
// para frente
d3f = (f(x0 + 3*h) - 3*f(x0 + 2*h) + 3*f(x0 + h) - f(x0)) / (h^3)
```

> => -0.6776054
> => -0.6798459
> => -0.6798683

--------------------------------------------------------------------------------------
11. Considere a seguinte tabela de dados:
x   | f(x)
--- | ------
0,2 | 2,415
0,4 | 2,637
0,6 | 2,907
0,8 | 3,193
1,0 | 3,381

utilize as fórmulas apropriadas para aproximar f'(0,4), f''(0,4) e f'''(0,4).

```
df = (2.907 - 2.415) / (2*0.2) = 1.23
d2f = (2.907 - 2*2.637 + 2.415) / (0.2^2) = 1.2000000
// para frente
d3f = (3.381 - 3*3.193 + 3*2.907 - 2.637) / (0.2^3) = -14.250000
// para tras
d3f = 
```

```
deff('y=f(x)', 'y=exp(-x^2)');
x = 1.5
h = 0.01
df = (f(x+h) - f(x-h)) / (2*h)
d2f = (f(x+h) - 2*f(x) + f(x-h)) / h^2
```

O erro das aproximações é proporcional ao h^2 em dif centradas e a h em progressiva e regressiva.

Exemplo do livro:
```
deff(’y=f(x)’,’y=exp(-x^2)’)  
x=1.5  
h=0.1  

//progressivas de ordem 1  
dp1 = (f(x+h)-f(x))/h  
//regressivas de ordem 1  
dr1 = (f(x)-f(x-h))/h  
//central de ordem 2  
dc2 = (f(x+h)-f(x-h))/(2*h)  
//progressivas de ordem 2  
dp2 = (-3*f(x)+4*f(x+h)-f(x+2*h))/(2*h)  
//regressivas de ordem 2  
dr2 = (f(x-2*h)-4*f(x-h)+3*f(x))/(2*h)  
//central de ordem 4  
dc4 = (f(x-2*h)-8*f(x-h)+8*f(x+h)-f(x+2*h))/(12*h)
```

--------------------------------------------------------------------------------------
12. Calcule a integral de f(x) = 3x + 5 no intervalo [1, 8] com a fórmula dos 
trapézios considerando h = 1.

```
function y=f(x)
    y = 3*x + 5
endfunction

function soma = trapezios(a, b, n)
    // a e b - limites da integracao
    // n - numero de pontos
    h = (b - a) / n
    x = linspace(a, b, n+1) // Cria um vetor com n+1 pontos entre a e b
    soma = 0
    
    for i = 1:n
        x1 = x(i)
        x2 = x(i+1)
        
        soma_parc = (f(x1)+f(x2))*h/2
        soma = soma + soma_parc
    end
endfunction

trapezios(1, 8, 7)
```

```
function y=f(x)
    y = 3*x + 5
endfunction

function soma = simpson_func(a,b,n)
    h = (b-a) / (2*n)
    x = linspace(a,b,n+1) // Cria um vetor com n+1 pontos entre a e b
    soma = 0
    
    for i = 1:n
        x1 = x(i)
        x3 = x(i+1)
        x2 = (x1+x3)/2
        
        soma_parc = (f(x1) + 4*f(x2) + f(x3))*h/3
        soma = soma + soma_parc
    end
endfunction

simpson_func(1,8,7)
```

--------------------------------------------------------------------------------------
13. Obtenha h para que por trapézios a integral de exp(-x^3) no intervalo [0,1]
tenha erro de truncamento menor do que 10^−5.

// a, b são os limites
// h é o passo
E_T(f, h) = (b - a) / 12 * h^2 * | max(f''(x)) |

M2 = | max(f''(x)) |
10^-5 > (b - a) / 12 * h^2 * M2
10^-5 > (1 - 0) / 12 * h^2 * M2
10^-5 > (h^2 * M2) / 12

exp(-x^3)
derivada 1: Regra da cadeia 
= exp(-x^3) * (-3x^2)

Derivada 2: Regra do produto e da cadeia
= (-6x) * exp(-x^3) + exp(-x^3) * (-3x^2) * (-3x^2)
= -6x*exp(-x^3) + exp(-x^3)*(9x^4)
= (-6*x + 9*x^4) * exp(-x^3)

```scilab
deff('y = f_2prima(x)', 'y = (9*x^4 - 6*x) * exp(-x^3)');
deff('y = f_2prima(x)', 'y = (9*x.^4 - 6*x) .* exp(-x.^3)');

x_vals = linspace(0, 1, 1000); // Cria 1000 pontos entre 0 e 1
y_vals = abs(f_2prima(x_vals)); // Calcula o módulo da segunda derivada

M2 = max(y_vals);
x_max = x_vals(find(y_vals == M2));

printf("O valor máximo de |f''(x)| ocorre em x ≈ %.4f\n", x_max);
printf("O valor de M2 é aproximadamente: %.4f\n", M2);
```

> => M2 = 2.1524

10^-5 > (h^2 * M2) / 12
(h^2 * 2.1524) / 12 < 10^-5
h^2 < (10^-5 * 12) / 2.1524
h < sqrt((10^-5 * 12) / 2.1524)
h < 0.0074667

n = (b-a)/h
n = 1/0.0074667

--------------------------------------------------------------------------------------
14. Encontre h por trapézios e por Simpson de forma que o erro máximo de 2^(-x) em [1, 3]
seja da ordem de 10^−6.

---

--------------------------------------------------------------------------------------
15. Resolver a integral de 1/(1+x^4) dx em [0,1] pelo método de Simpson com DIGSE 4.

```scilab
function y=f(x)
    y = 1/(1+x^4)
endfunction

function soma = simpson_func(a,b,n)
    h = (b-a) / (2*n)
    printf("\n h: %f", h)
    x = linspace(a,b,n+1) // Cria um vetor com n+1 pontos entre a e b
    soma = 0
    
    for i = 1:n
        x1 = x(i)
        x3 = x(i+1)
        x2 = (x1+x3)/2
        
        soma_parc = (f(x1) + 4*f(x2) + f(x3))*h/3
        soma = soma + soma_parc
    end
endfunction

function res = simpson_max_dig(a, b, max_e)
    d = 10;
    n = 3;

    while d > max_e
        s = simpson_func(a, b, n);
        n = n + 1;
        s1 = simpson_func(a, b, n);
        d = abs(s1 - s);
    end
    printf("\n n: %d", n);
    
    res = s1;
endfunction

simpson_max_dig(0,1,10^-4)

```

--------------------------------------------------------------------------------------
16. Por Gauss para n = 2, calcule: integral(x^5) em [-1, 1]

```
function y=f(x)
    y = x^5
endfunction

disp(trapezios(-1, 1, 2));
disp(simpson_func(-1,1, 2));
```

> => 0

--------------------------------------------------------------------------------------
17. Calcule a integral de exp(-4*x) em [2, 8]

```
function y=f(x)
    y = exp(-4*x)
endfunction

trapezios(2, 8, 60)
simpson_func(2, 8, 60)
simpson_max_dig(2, 8, 10^-10)
```

> => 0.0000850
> => 0.0000839
> => 0.0000839 (n = 53)

--------------------------------------------------------------------------------------
18. Calcule PI a partir de: PI/4 = integral(1/(1 + x^2)) em [0, 1]

```
format(10);
function y=f(x)
    y = 1/(1 + x^2)
endfunction

printf("\n%.15f", simpson_max_dig(0, 1, 10^-10))
= 0.7853981 * 4
= 3.1415924
```

--------------------------------------------------------------------------------------
19. 

--

--------------------------------------------------------------------------------------
20. Considere uma estrutura governada por mẍ + cẋ + kx = f (x)
Obtenha x(t) numericamente quando m = 5, k = 60, c = 0,6m + 0,4k e f(x) = x. 

Adote:
∆t = 0,1 
x(0) = 0 
ẋ(0) = 1.

5*ẍ + (0.6*5 + 0.4 * 60)*ẋ + 60*x = x
5*ẍ + (3 + 24)*ẋ + 60*x = x
5*ẍ + 27*ẋ + 60*x = x
5*ẍ + 27*ẋ + (60 - 1)*x = 0

1. Redução de Ordem: 
Transformar a EDO de 2ª ordem em um sistema de duas EDOs de 1ª ordem.

2. Solução Numérica

