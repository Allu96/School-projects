function [Trees,Err] = MyRandomForest(X,y,B,d,nmin)
% random forest for binary classification problem 
% 
% INPUT: 
%   X       N x p  feature matrix 
%   y       N x 1 matrix of class labels (values -1 or 1)
%   B       number of Bootstrap samples (bags)
%   d       number of features in each split
%   nmin    minimum node size 
%
% OUTPUT:
%   Trees  a cell array of length B where each cell is a classification tree
%   Err    OOB training error (vector of length B)
%--------------------------------------------------------------------------

N = size(X,1);      % Sample length
Trees = cell(1,B);  % initialize the cell array where to save the bagged trees
Err = zeros(1,B);   % initialize the OOB error rates 

% ... 

%% start the bagging iterations 
for b = 1:B
    
    % Line 2: Draw a boostrap sample 
    
    % Line 3-6: fit the classification decision tree the bootstrap training data    
    
   % Extra line : update the OOB training error 
  
end
% DONE
