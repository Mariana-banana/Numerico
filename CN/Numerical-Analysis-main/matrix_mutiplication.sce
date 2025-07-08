// define matrices sizes

rows_1 = 3
cols_1 = 3
rows_2 = 3 // must be equal than cols_1
cols_2 = 2

// attribute values

M1 = [3 1 7; 8 2 5; 9 6 4];
M2 = [2 4; 3 6; 1 5];
R = zeros(rows_1, cols_2);

// compute multiplication

for i = 1:cols_2
    for j = 1:rows_1
        for k = 1:cols_1
            R(j,i) = R(j,i) + (M1(j,k) * M2(k,i))
        end
    end
end

disp(M1, M2, R) // display result of the implemented algorithm
disp(M1*M2) // display result of the scilab implementation
