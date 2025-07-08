// define matrix coefficients

A = [10 2 -1; -3 -6 2; 1 7 5];

// verify diagonal dominance

function [flag] = is_diagonal_dominant(A)
    n = size(A,1);
    flag = %t;

    for i = 1:n
        sigma = sum(abs(A(i, :))) - abs(A(i,i));

        if abs(A(i,i)) <= sigma then
            flag = %f;
            return;
        end
    end
endfunction

disp(is_diagonal_dominant(A))