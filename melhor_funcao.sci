function melhor_modelo = analise(X, Y)
    
    // --- Reta ---
    buf_reta = diff(Y) ./ diff(X);
    cv_reta = stdev(buf_reta) / abs(mean(buf_reta));
    disp("Reta (diff Y / diff X):")
    disp(buf_reta)
    disp("CV Reta:")
    disp(cv_reta)
    
    // --- Parábola (usando diferenças quadráticas) ---
    buf_para = (diff(Y)).^2 ./ diff(X.^2);
    cv_para = stdev(buf_para) / abs(mean(buf_para));
    disp("Parábola (diff Y^2 / diff X^2):")
    disp(buf_para)
    disp("CV Parábola:")
    disp(cv_para)
    
    // --- Cúbica (usando diferenças cúbicas) ---
    buf_cub = (diff(Y)).^3 ./ diff(X.^3);
    cv_cub = stdev(buf_cub) / abs(mean(buf_cub));
    disp("Cúbica (diff Y^3 / diff X^3):")
    disp(buf_cub)
    disp("CV Cúbica:")
    disp(cv_cub)
    
    // --- Exponencial ---
    buf_exp = diff(log(Y)) ./ diff(X);
    cv_exp = stdev(buf_exp) / abs(mean(buf_exp));
    disp("Exponencial (diff ln(Y) / diff X):")
    disp(buf_exp)
    disp("CV Exponencial:")
    disp(cv_exp)
    
    // --- Potência ---
    buf_pot = diff(log(Y)) ./ diff(log(X));
    cv_pot = stdev(buf_pot) / abs(mean(buf_pot));
    disp("Potência (diff ln(Y) / diff ln(X)):")
    disp(buf_pot)
    disp("CV Potência:")
    disp(cv_pot)
    
    // Armazenar CVs para comparar
    cvs = [cv_reta, cv_para, cv_cub, cv_exp, cv_pot];
    modelos = ["Reta", "Parábola", "Cúbica", "Exponencial", "Potência"];
    
    // Encontrar índice do menor CV
    [min_cv, idx] = min(cvs);
    
    disp("Melhor modelo baseado no menor coeficiente de variação (CV): " + modelos(idx));
    
    // Plotar os pontos
    clf();
    plot(X, Y, 'go');
    xtitle("Análise dos dados");
    
    // Retornar o nome do melhor modelo
    melhor_modelo = modelos(idx);
    
endfunction

// Dados do problema da Temperatura vs. Pressão
P = [5, 15, 25, 35]; // Variável X
T = [10, 15, 20, 13]; // Variável Y

melhor_ajuste = analise(P, T)
