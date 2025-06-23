// Limpa o console e as variáveis
clc;
clear;

//=============================================================================
// FUNÇÃO PRINCIPAL
// Calcula o 'h' e 'n' para os métodos de Simpson e dos Trapézios
//=============================================================================
function [h_simpson, n_simpson, h_trapezio, n_trapezio] = calcularH(f, f2, f4, a, b, erro_max)
    // f:  A função a ser integrada (ex: f(x) = 1/(2*x))
    // f2: A segunda derivada da função f(x)
    // f4: A quarta derivada da função f(x)
    // a, b: O intervalo de integração [a, b]
    // erro_max: O erro máximo tolerado (ex: 1e-6)

    // --- Cálculo para o Método de Simpson ---
    disp("--- Método de Simpson ---");

    // Para encontrar M4 (máximo de |f''''(x)| em [a,b]), avaliamos em vários pontos
    x_vals = linspace(a, b, 2000); // Cria um vetor de pontos no intervalo
    M4 = max(abs(f4(x_vals)));     // Calcula o máximo da 4ª derivada

    // Fórmula do erro para Simpson: E <= (b-a)^5 * M4 / (180 * n^4)
    // Isolando n: n >= ((b-a)^5 * M4 / (180 * E))^(1/4)
    numerador_S = (b-a)^5 * M4;
    denominador_S = 180 * erro_max;
    n_simpson_calc = (numerador_S / denominador_S)^(1/4);

    // n precisa ser o próximo inteiro par
    n_simpson = ceil(n_simpson_calc);
    if modulo(n_simpson, 2) <> 0 then
        n_simpson = n_simpson + 1; // Se for ímpar, soma 1 para se tornar par
    end

    // Calcula o passo h
    h_simpson = (b - a) / n_simpson;

    // Mostra os resultados para Simpson
    disp(msprintf("Máximo da 4ª derivada (M4): %f", M4));
    disp(msprintf("Número de intervalos (n) calculado: %f", n_simpson_calc));
    disp(msprintf("Número de intervalos (n) a ser usado (inteiro par): %d", n_simpson));
    disp(msprintf("Passo (h) necessário: %f\n", h_simpson));


    // --- Cálculo para o Método dos Trapézios ---
    disp("--- Método dos Trapézios ---");

    // Para encontrar M2 (máximo de |f''(x)| em [a,b]), usamos o mesmo método
    M2 = max(abs(f2(x_vals)));     // Calcula o máximo da 2ª derivada

    // Fórmula do erro para Trapézios: E <= (b-a)^3 * M2 / (12 * n^2)
    // Isolando n: n >= sqrt((b-a)^3 * M2 / (12 * E))
    numerador_T = (b-a)^3 * M2;
    denominador_T = 12 * erro_max;
    n_trapezio_calc = sqrt(numerador_T / denominador_T);

    // n precisa ser o próximo inteiro
    n_trapezio = ceil(n_trapezio_calc);

    // Calcula o passo h
    h_trapezio = (b - a) / n_trapezio;

    // Mostra os resultados para Trapézios
    disp(msprintf("Máximo da 2ª derivada (M2): %f", M2));
    disp(msprintf("Número de intervalos (n) calculado: %f", n_trapezio_calc));
    disp(msprintf("Número de intervalos (n) a ser usado (inteiro): %d", n_trapezio));
    disp(msprintf("Passo (h) necessário: %f\n", h_trapezio));

endfunction


//=============================================================================
// EXEMPLO DE USO: Resolvendo a questão da imagem
//=============================================================================

// 1. Defina as funções usando 'deff'
// IMPORTANTE: Use operadores elemento a elemento (./, .*, .^)
// para que as funções funcionem com vetores.
deff('y = f(x)',  'y = 1 ./ (2*x)');
deff('y = f2(x)', 'y = 1 ./ (x.^3)');      // Segunda derivada: 1/x³
deff('y = f4(x)', 'y = 12 ./ (x.^5)');     // Quarta derivada: 12/x⁵

// 2. Defina os parâmetros do problema
a = 1;
b = 3;
erro_desejado = 1e-6; // 10^-6

// 3. Chame a função para obter os resultados
[h_s, n_s, h_t, n_t] = calcularH(f, f2, f4, a, b, erro_desejado);
