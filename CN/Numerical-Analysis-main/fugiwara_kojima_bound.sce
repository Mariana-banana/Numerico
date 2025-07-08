// define P(x) coefficients

coefficients = [1 1 -9 -1 20 -12]; // P(x) = x^5 + x^4 - 9x^3 - x^2 + 20x - 12 

// apply fugiwara's bound

function [bound] = fugiwara_bound(coefficients, degree)
    k = [];

    for i = 2:degree+1
        exponent = 1/(i-1);
        k($+1) = abs(coefficients(i)/coefficients(1))^exponent;
    end

    k = gsort(k);
    bound = abs(2*(k(1)));
endfunction

// apply kojima's bound

function [bound] = kojima_bound(coefficients, degree)
    k = [];

    for i = 2:degree+1
        exponent = 1/(i-1);
        k($+1) = abs(coefficients(i)/coefficients(1))^exponent;
    end

    k = gsort(k);
    bound = abs(k(1)+k(2));
endfunction

degree = length(coefficients) - 1;

disp("Fugiwara''s bound: " + string(fugiwara_bound(coefficients, degree)))
disp("Kojima''s bound: " + string(kojima_bound(coefficients, degree)))