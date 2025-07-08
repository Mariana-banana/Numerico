// define functions vector

function f = F(x)
    f1 = x(1)^2 + x(2)^2 - 4;
    f2 = exp(x(1)) + x(2) - 1;
    f = [f1; f2];
endfunction

// compute jacobian matrix

function [J] = get_jacobian(x)
    df1_dx = 2 * x(1);
    df1_dy = 2 * x(2);
    df2_dx = exp(x(1));
    df2_dy = 1;
    J = [df1_dx, df1_dy; df2_dx, df2_dy];
endfunction

// apply newthon method

function [x] = newthon_method(x0, tolerance, max_iterations)
    x = x0;

    for k = 1:max_iterations
        f_values = F(x);
        J_values = get_jacobian(x);
        
        dx = -J_values \ f_values;
        x = x + dx;
        
        if norm(dx, "inf") < tolerance then
            break
        end
    end
endfunction

disp(newthon_method([1; 1], 1e-6, 20))
