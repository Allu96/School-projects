function [G,alpha] = MyAdaBoostM1(X,y,M)
% AdaBoost.M1 algorithm for binary classification problem, when the 
% weak learner is a stump. 
% 
% INPUT: 
%   X       N x p  feature matrix 
%   y       N x 1 matrix of class labels (-1 or 1)
%   M       number of weak learners (boosting aggregations)
%
% OUTPUT:
%  G       M trees  (cell)
%  alpha   M x 1 vector of weights
%
%  Joe Student / Student #
%--------------------------------------------------------------------------

N = length(y);         % Sample length 
alpha = zeros(M,1);    % initialize the alpha
G = cell(M,1);         % initialize the cell of stump trees
w = ones(N,1)./N;      % Initialize the observation weights

% start the boosting iteration 
for m = 1:M
    
    % Line 2. Fit the stump to the training data using weights w.     
   
    % Line 3. Compute the error:   
    
    % Line 4: Compute alpha-s:
    
    % Line 5:  Update the weights w_i, i=1,...,N   
    
end
% all done