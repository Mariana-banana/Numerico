// define matrix A and vector b

A = [10 2 -1; -3 -6 2; 1 1 5];

b = [27; -61.5; -21.5];

// apply gauss-seidel method

function [x1] = gauss_seidel_method(A, b, x0, tolerance, max_iterations)
    n = length(b);
    x1 = x0;
    
    for k = 1:max_iterations
        x0 = x1;

        for i = 1:n
            sigma = 0;

            for j = 1:n
                if j ~= i then
                    sigma = sigma + A(i,j) * x1(j);
                end
            end

            x1(i) = (b(i) - sigma) / A(i,i);
        end

        if norm(x1 - x0, %inf) < tolerance then
            return;
        end
    end
endfunction

disp(gauss_seidel_method(A, b, [0; 0; 0], 1e-3, 100))