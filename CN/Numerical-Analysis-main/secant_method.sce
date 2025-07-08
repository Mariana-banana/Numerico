// define f(x)

function [y] = f(x)
    y = x.^3 + 2*x.^2 - 3*x + 1;
endfunction

// apply secant method

function [root] = secant_method(x0, x1, tolerance, max_iterations)
    for i = 1:max_iterations
        if abs(f(x1)) < tolerance then
            root = x1;
            return;
        end

        aux = x1;
        x1 = x1 - ((x1-x0)*f(x1)/(f(x1)-f(x0)));
        x0 = aux;
    end

    root = x1;
endfunction

disp(secant_method(-3.1, -2.9, 1e-6, 100))