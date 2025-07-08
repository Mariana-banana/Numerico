// define interval

x = -5:0.1:5;

// define functions

y1 = sin(x);
y2 = cos(x);

// plot

plot(x, y1, 'r-', x, y2, 'b--');
legend("sin(x)", "cos(x)")
xlabel("x")
ylabel("y")
title("Sine e Cosine")
