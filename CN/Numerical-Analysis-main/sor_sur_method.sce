// define matrix A and vector b

A = [10 2 -1; -3 -6 2; 1 1 5];

b = [27; -61.5; -21.5];

// apply sor/sur method

function [x1] = sor_sur_method(A, b, x0, omega, tolerance, max_iterations)
    n = size(A, 1);
    x1 = x0;

    for k = 1:max_iterations
        for i = 1:n
            sigma = 0;

            for j = 1:n
                if j <> i then
                    sigma = sigma + A(i,j)*x1(j);
                end
            end

            x1(i) = (1 - omega)*x0(i) + (omega/A(i,i))*(b(i) - sigma);
        end

        if norm(x1 - x0, 2) / norm(x1, 2) < tolerance then
            return
        end

        x0 = x1;
    end
endfunction

disp(sor_sur_method(A, b, [0; 0; 0], 0.5, 1e-3, 100))