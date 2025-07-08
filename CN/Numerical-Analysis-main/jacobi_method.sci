// define matrix A and vector b

A = [10 2 -1; -3 -6 2; 1 1 5];

b = [27; -61.5; -21.5];

// apply jacobi method

function [x] = jacobi_method(A, b, x0, tolerance, max_iterations)
    n = length(b);
    x1 = x0;

    for k = 1:max_iterations
        x1(1) = (b(1) - A(1,2:n) * x(2:n)) / A(1,1);

        for i = 2:n-1
            x1(i) = (b(i) - A(i, 1:i-1) * x(1:i-1) - A(i, i+1:n) * x(i+1:n) ) / A(i,i);
        end

        x1(n) = (b(n) - A(n,1:n-1) * x(1:n-1) ) / A(n,n);

        if norm(x1 - x0, %inf) < tolerance then
            return;
        end
    end
endfunction

disp(jacobi_method(A, b, [0; 0; 0], 1e-3, 100))