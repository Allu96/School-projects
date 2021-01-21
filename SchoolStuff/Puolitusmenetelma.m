% Bisection method for 1-dimensional data

k = 1000;
%x = 1;   % Alkuarvaus
a = -10;
b = 10;
f = @(x) 2*x^3 - 5*x^2 + 9*x + 3;
tarkka = -0.28359; % Wolframista
if (f(a) < 0) && (f(b) < 0)
    disp('Nollakohta ei valilla.')
elseif (f(a) > 0) && (f(b) > 0)
    disp('Nollakohta ei valilla.')
else
    for i = 1:k
        r = (a+b)/2;
        
        if a == b  
            break
        end
        
        if (f(a) < 0) && (f(r) > 0)
            b = r;
        elseif (f(a) > 0) && (f(r) < 0)
            b = r;
        elseif (f(b) < 0) && (f(r) > 0)
            a = r;
        elseif (f(b) > 0) && (f(r) < 0)
            a = r;
        end
            
    end
end
r
abs_virhe = abs(tarkka - r)
suht_virhe = abs((tarkka - r)/r)
