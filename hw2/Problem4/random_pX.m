% control the randomness for reproduceability 
rng(314159);

p0_params = rand(1,2);
p0_params = bsxfun(@rdivide,p0_params,sum(p0_params,2));

p1_0_params = rand(2,2);
p1_0_params = bsxfun(@rdivide,p1_0_params,sum(p1_0_params,2));

p2_params = rand(1,2);
p2_params = bsxfun(@rdivide,p2_params,sum(p2_params,2));

p3_0_params = rand(2,2);
p3_0_params = bsxfun(@rdivide,p3_0_params,sum(p3_0_params,2));

p4_0_params = rand(2,2);
p4_0_params = bsxfun(@rdivide,p4_0_params,sum(p4_0_params,2));

p5_134_params = rand(8,2);
p5_134_params = bsxfun(@rdivide,p5_134_params,sum(p5_134_params,2));

p6_24_params = rand(4,2);
p6_24_params = bsxfun(@rdivide,p6_24_params,sum(p6_24_params,2));

p7_13_params = rand(4,2);
p7_13_params = bsxfun(@rdivide,p7_13_params,sum(p7_13_params,2));

p8_134_params = rand(8,2);
p8_134_params = bsxfun(@rdivide,p8_134_params,sum(p8_134_params,2));

p9_134_params = rand(8,2);
p9_134_params = bsxfun(@rdivide,p9_134_params,sum(p9_134_params,2));

p10_2_params = rand(2,2);
p10_2_params = bsxfun(@rdivide,p10_2_params,sum(p10_2_params,2));

p11_124_params = rand(8,2);
p11_124_params = bsxfun(@rdivide,p11_124_params,sum(p11_124_params,2));
