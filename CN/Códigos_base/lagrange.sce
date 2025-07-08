// lagrange produz um sistema linear diagonal
function y=L(X,x,k)
    n=size(x,1);
    y=1;
    for j=1:n
        if(k <> j)
            y=y.*(X-x(j))/(x(k)-x(j))
        end
    end
endfunction

x = [2 3] '
y= [4 7]'
n=length(x)

//plot(x,y,'ro-'),xgrid

X=2.5
p=0
for k=1:n
    p=p+y(k)*L(X,x,k);
end
disp(p)

nCond = norm(p)*norm(inv(p))
format("v", 25)
disp(nCond)



//ex:
//Interpole os pontos dados por x=[1, 2, 3, 4] e y=[3, 4, 7, 6] em x=2.5 utilizando 2 pontos.
//x = [2 3]
//y = [4 7]
//p = 0
//X = 2.5
