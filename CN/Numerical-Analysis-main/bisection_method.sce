// define f(x)

function [y] = f(x)
    y = x.^3 + 2*x.^2 - 3*x + 1;
endfunction

// apply bisection method

function [root] = bisection_method(a, b, tolerance, max_iterations)
    if f(a) * f(b) >= 0 then
        error("This interval may not contain a root")
    end

    for i = 1:max_iterations
        xm = (a+b)/2;

        if abs(f(xm)) < tolerance then
            root = xm;
            return;
        end

        if f(xm)*f(a) < 0 then
            b = xm;
        else
            a = xm;
        end
    end

    root = xm;
endfunction

disp(bisection_method(-4, -2, 1e-6, 100))