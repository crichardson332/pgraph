function [x] = outcome_to_assignments(outcome)
if outcome < 0 || outcome > 4095
    error("Outcome out of range [0,4095]")
end

x = str2double(regexp(num2str(dec2bin(outcome)),'\d','match'));
x = [zeros(1, 12-length(x)) x];

end

