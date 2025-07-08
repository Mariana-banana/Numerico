clear;
x=0:1:2 // O X, claramente
x = x'
y = [exp(x/14)-1.5] // Y do problema

n=size(x,1);

M=[x x.^2] //x e x^2 polinomio (formato bx + cx^2), se quiser a+bx+cx^2 ficaria [x.^0 x x.^2]
disp(M)
disp(y)
cu = M' * M

pau = M' * y //SE VOCÊ CRIOU Y COM PONTOS SEPARADOS (SEM SER FUNÇÃO DE X), AQUI TEM QUE SER y'
            //alternativamente, só adiciona o ' (ou tira ele) se der inconsistent rows
            //isso aí, boa sorte nas provas :0


//mesma ordem declarada 
disp(inv(cu)*pau)
