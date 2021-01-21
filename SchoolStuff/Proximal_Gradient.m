% Proximal Gradient algorithm

% maximum number of iterations
k = 1000;

% dimension
n = 100;

% initial value of x
x_0 = ones(n,1);

% generating random vector and matrix
sparse = 3;
l = 4*sparse;
B = randn([l n]);
B = B./vecnorm(B,2,2);
A = B'*B;


% optimal value of x
x_value = zeros(n,1);
x_value(3) = randn;
x_value(33) = randn;
x_value(63) = randn;

% generating decent b
b = A*x_value;

% tolerance parameter
Gradtol = 10e-5;

% function to be minimized
f = @(x) (1/2)*x'*A*x - b'*x;

% initializing parameters
lambda = 1;
beta = 0.5;

%gamma
gamma_max = norm(A'*b,'inf');
gamma = 0.1*gamma_max;

% gradient
%grad = @(x) A*x - b; 

% save values of x
x_prev = [];

% step-size
a = 1/trace(A);

% initializing norm to express difference 
% between optimal x and iterated x
pnorm = zeros(length(x_0),1);

% iterations

for i = 1:k
    while 1 
        grad = A*x_0 - b;
        v = x_0 - lambda*grad;
        %x_new = v - lambda*gamma;
        x_new = max(0, v - lambda*gamma) - max(0, -v - lambda*gamma);
        norm(x_new);
        %x_new = norm(x_0 - lambda*grad + lambda*gamma,1);
        if f(x_new) <= f(x_0) + grad'*(x_new - x_0) + (1/(2*lambda))*norm(x_new - x_0)^2
            break;
        end
        lambda = beta*lambda;
    end
    x_prev(:,i) = x_0;
    x_0 = x_new;      % update x
    norm(x_0);
    pnorm(i) = (norm(x_prev(:,i) - x_value));
end   
   
%plot
figure(1)
semilogy(1:length(x_prev),pnorm, 'Linewidth',2)
title('Proximal Gradient')
xlabel('k')
ylabel('log norm')