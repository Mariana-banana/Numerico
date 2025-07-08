function S = trapezio(a,b,n) //a = inicio b = fim n = numero de intervalos
    h = (b-a)/n // tamanho de cada intervalo
    x = linspace(a,b,n+1) //calcula os pontos (1,2,3,...) dado o intervalo
    S = 0
    for i = 1:n
        x1 = x(i)
        x2 = x(i+1)
        
        A1 = 1/2
        A2 = 1/2
        
        dS = (f(x1)+f(x2))/2*h //área do trapézio <<<< versão curta, a fórmula bonita é (A1*f(x1)+A2*f(x2))/h, sendo que A1 = A2 = 1/2 >>>>
        
        S = S+dS //área total
    end
endfunction

function y = f(x) // aqui define a função a ser integrada
    y = x^3 - 14*x
endfunction

// pra rodar, exemplo: trapezio(1,10,100); Integra a função f(x) de 1 a 100 usando 100 intervalos
