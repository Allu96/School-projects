% Gradient_Descent algorithm

% maximum number of iterations
k = 1000;

% dimension
n = 100;

% initial value of x
x_0 = ones(n,1);

% generating random vector and matrix
b = randn(n,1);
A = randn(n);

% symmetric and semidefinite matrix
A = A*A';

% optimal value of x
tic
x_value = A\b;
toc

% tolerance parameter
Gradtol = 10e-5;

% function to be minimized
f = @(x) (1/2).*x'.*A.*x - b'.*x;

% gradient
grad = @(x) A*x - b;

% save values of x
x_prev = [];

% step-size
a = 1/trace(A);

% initializing norm to express difference 
% between optimal x and iterated x
pnorm = zeros(length(x_0),1);
tic

% iterations
for i = 1:k
 if norm(grad(x_0)) < Gradtol
 break;
 end
 v = -grad(x_0);
 v = a*v;
 x_prev(:,i) = x_0;
 x_0 = x_0 + v;            % update x
 pnorm(i) = (norm(x_prev(:,i) - x_value));
end
toc

%plot
figure(1)
semilogy(1:length(x_prev),pnorm, 'Linewidth',2)
title('Gradient Descent')
xlabel('k')
ylabel('norm')

%Elapsed time is 3.710801 seconds. 
