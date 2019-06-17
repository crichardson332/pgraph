%% This file calculates the probaility of every possible assignment

n_pts = 4096;
pXarr = zeros(n_pts, 1);
for outcome = 0:n_pts-1
    % transform a decimal number into binary representation, and then put
    % the binary bits into an array of bits
    asgn_bin = str2double(regexp(num2str(dec2bin(outcome)),'\d','match'));
    asgn_bin = [zeros(1, 12-length(asgn_bin)) asgn_bin];
    pXarr(outcome+1) = assignments_to_pX(outcome_to_assignments(outcome));
end

% this sum should be 1
sum_pX = sum(pXarr)






