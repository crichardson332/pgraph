n_pts = 4096;
pXarr = zeros(1, n_pts);
for assignment = 0:n_pts-1
    asgn_bin = str2double(regexp(num2str(dec2bin(assignment)),'\d','match'));
    asgn_bin = [zeros(1, 12-length(asgn_bin)) asgn_bin];
    pXarr(assignment+1) = problem4p1a_joint(asgn_bin);
end




