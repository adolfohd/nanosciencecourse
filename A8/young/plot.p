set style circle radius 10;
set terminal pdf;
set output 'young.pdf'; 

# set terminal tex
# set output 'youn.tex'

# set terminal epslatex color
# set output 'youn.tex'

# set xlabel '$\epsilon = \frac{ \Delta L}{L}$'
set xlabel 'epsilon = dL/L'
# set ylabel '$\sigma$'
set ylabel '[GPa]'

f(x) = m*x + b
FIT_LIMIT = 1e-6
fit f(x) 'eos' using 1:2 via m, b
set title sprintf("y= %g x + %g",m,b)


# plot 'eos' using 1:2 with lines title '$pressure_x$ VS $\Delta L$'
plot 'eos' using 1:2 with lines title 'sigma_x'