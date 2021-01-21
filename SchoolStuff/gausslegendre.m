function [x,w] = gausslegendre(alpha,beta)
%
% Gauss-Legendre kvadratuuri välillä [-1,1].
% x on sarake
% w on rivi
%
[Q,Lambda] = eig(diag(beta,1)+diag(alpha,0)+diag(beta,-1));
[x,i] = sort(diag(Lambda));
Qtop = Q(1,i);

w = 2*Qtop.^2;
end