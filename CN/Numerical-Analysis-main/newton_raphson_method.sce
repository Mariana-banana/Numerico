// define f(x) and f'(x)

function [y] = f(x)
    y = x.^3 + 2*x.^2 - 3*x + 1;
endfunction

function [y] = f_(x)
    y = 3*x.^2 + 4*x - 3;
endfunction

// apply newton-raphson method

function [root] = newton_raphson_method(x0, tolerance, max_iterations)
    for i = 1:max_iterations
        if abs(f(x0)) < tolerance then
            root = x0;
            return;
        end

        x0 = x0 - (f(x0)/f_(x0));
    end

    root = x0;
endfunction

disp(newton_raphson_method(-3, 1e-6, 100))