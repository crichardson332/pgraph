function pX = problem4p1a_joint(x)

run('problem4p1a');

idx0 = [1, x(1) + 1];
idx1_0 = [x(1) + 1, x(2) + 1];
idx2 = [1, x(3) + 1];
idx3_0 = [x(1) + 1, x(4) + 1];
idx4_0 = [x(1) + 1, x(5) + 1];
idx5_134 = [x(2) + 2*x(4) + 4*x(5) + 1, x(6) + 1];
idx6_24 = [x(3) + 2*x(5) + 1, x(7) + 1];
idx7_13 = [x(2) + 2*x(4) + 1, x(8) + 1];
idx8_134 = [x(2) + 2*x(4) + 4*x(5) + 1, x(9) + 1];
idx9_134 = [x(2) + 2*x(4) + 4*x(5) + 1, x(10) + 1];
idx10_2 = [x(3) + 1, x(11) + 1];
idx11_124 = [x(2) + 2*x(3) + 4*x(5) + 1, x(12) + 1];

p0 = p0_params(idx0(1), idx0(2));
p1_0 = p1_0_params(idx1_0(1), idx1_0(2));
p2 = p2_params(idx2(1), idx2(2));
p3_0 = p3_0_params(idx3_0(1), idx3_0(2));
p4_0 = p4_0_params(idx4_0(1), idx4_0(2));
p5_134 = p5_134_params(idx5_134(1), idx5_134(2));
p6_24 = p6_24_params(idx6_24(1), idx6_24(2));
p7_13 = p7_13_params(idx7_13(1), idx7_13(2));
p8_134 = p8_134_params(idx8_134(1), idx8_134(2));
p9_134 = p9_134_params(idx9_134(1), idx9_134(2));
p10_2 = p10_2_params(idx10_2(1), idx10_2(2));
p11_124 = p11_124_params(idx11_124(1), idx11_124(2));

pX = p0 * p1_0 * p2 * p3_0 * p4_0 * p5_134 * p6_24 * p7_13 * p8_134 * p9_134 * p10_2 * p11_124;

end
