// define f(x) and f'(x)

function [y] = f(x)
    y = x.^3 + 2*x.^2 - 3*x + 1;
endfunction

function [y] = f_(x)
    y = 3*x.^2 + 4*x - 3;
endfunction

// apply bolzano's theorem

function [flag] = is_derivative_sign_constant(a, b)
    x = linspace(a, b, 100);
    y = f_(x);
    
    if and(y > 0) then
        flag = %t;
    elseif and(y < 0) then
        flag = %t;
    else
        flag = %f;
    end
endfunction

function bolzano_theorem(a, b)
    if f(a)*f(b) < 0 then
        disp("There is an odd number of real roots in this interval")

        if is_derivative_sign_constant(a, b) then
            disp("There is exactly one real root in the interval")
        end

    elseif f(a)*f(b) > 0 then
        disp("There is an even number of real roots in this interval")

        if is_derivative_sign_constant(a, b) then
            disp("There are no real roots in the interval")
        end
    end
endfunction

bolzano_theorem(-4, -2)