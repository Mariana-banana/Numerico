// O que isso faz? Integra em um intervalo com o método de gauss e x nodos
// defina a função lá embaixo y = f(x)
function S = gaussiana(a, b, num_nodos, n) //início, fim do intervalo, número de nodos, número de intervalos.
    h = (b-a)/n
    x = linspace(a,b,n+1)
    
    select num_nodos
    case 1 then
        w = [2]; t = [0]
    case 2 then
        w = [1 1]; t = [-sqrt(3)/3 sqrt(3)/3]
    case 3 then
        w = [5/9 8/9 5/9]; t = [-sqrt(3/5) 0 sqrt(3/5)]
    case 4 then
        w = [0 0 0 0]; t = [0 0 0 0]
        w(1) = (18 - sqrt(30))/36;   t(1) = -sqrt((3 + 2*sqrt(6/5))/7)
        w(2) = (18 + sqrt(30))/36;   t(2) = -sqrt((3 - 2*sqrt(6/5))/7)
        w(3) = (18 + sqrt(30))/36;   t(3) = sqrt((3 - 2*sqrt(6/5))/7)
        w(4) = (18 - sqrt(30))/36;   t(4) = sqrt((3 + 2*sqrt(6/5))/7)   
    end
    w1 = 5/9; t1 = -sqrt(3/5)
    w2 = 8/9; t2 = 0
    w3 = w1;  t3 = -t1
    
    S = 0
    S2 = 0
    for i = 1:n
        alpha = (x(i+1)-x(i))/2
        bet = (x(i+1)+x(i))/2
        
        x1 = alpha*t1+bet
        x2 = alpha*t2+bet
        x3 = alpha*t3+bet
        
        xcu = alpha.*t+bet
        xpau = matrixfun(f,xcu) // aplica a função F em cada X
        
        A2 = sum(w.*xpau) * h/2 // equivale a (w1*f(x1) + w2*f(x2) + w3*f(x3) + w4*f(x4)) * h/2
        S2 = S2+A2
        
        S = S2
    end
endfunction

function y = f(x)
    y = sin(sin(sin(x)))
endfunction

function B = matrixfun(func,A)
    for i = 1 : size(A,'r')
        for j = 1 : size(A,'c')
            B(i,j) = func(A(i,j))
        end
    end
endfunction
