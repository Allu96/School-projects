function y = seriesexp(x)
oldsum = 0;
newsum = 1;
term = 1;
n = 0;

while newsum ~= oldsum
    n = n + 1;
    term = term * x / n;
    oldsum = newsum;
    newsum = newsum + term;
end;
y = newsum;
end