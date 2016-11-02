set style circle radius 10;
set terminal pdf;
set output 'young.pdf'; 

f(x) = m*x + b
FIT_LIMIT = 1e-6
fit f(x) 'eos' using 1:2 via m, b

plot 'eos' using 1:2 with lines