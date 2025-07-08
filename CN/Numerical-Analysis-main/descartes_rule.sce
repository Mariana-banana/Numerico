// define P(x) coefficients

positive_coefficients = [3 2 -1 -1]; // P(x) = 3x^3 + 2x^2 - x - 1
negative_coefficients = [-3 2 1 -1]; // P(-x) = -3x^3 + 2x^2 + x - 1

// apply descartes' rule

function [sign] = get_sign(n)
    if n < 0 then
        sign = '-';
    elseif n > 0 then
        sign = '+';
    else
        sign = '0';
    end
endfunction

function [sign_changes] = descartes_rule(coefficients)
    sign_changes = 0;
    current_sign = get_sign(coefficients(1));

    for i = 2:length(coefficients)
        next_sign = get_sign(coefficients(i));

        if (next_sign ~= current_sign & next_sign ~= '0') then
            sign_changes = sign_changes + 1;
            current_sign = next_sign;
        end
    end
endfunction

disp("Maximum number of positive real roots (T): " + string(descartes_rule(positive_coefficients)))
disp("Maximum number of negative real roots (T): " + string(descartes_rule(negative_coefficients)))

disp("It can be: T-2, T-4, ...")