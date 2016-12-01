rm(list = ls())
a <- c(
  0.698000, 0.000000, 0.000000,
  0.000000, 1.208971, 0.000000,
  0.698000, 2.417943, 0.000000,
  0.000000, 3.626914, 0.000000,
  0.698000, 4.835886, 0.000000,
  0.000000, 6.044857, 0.000000,
  11.168000, 47.149887, 0.000000,
  10.470000, 48.358859, 0.000000,
  11.168000, 49.567830, 0.000000
  )

m <- matrix(a, 9, 3, byrow = T)

print(m)
svg("/media/fito/Windows/Users/fitoh/Documents/code/nanosciencecourse/project/demo0/graphene.demo.svg")
plot(m[,1], m[,2], type = "p", xlab = "x-axis", ylab = "y-axis")
title("Plot of obtained array of carbon positions")
dev.off()

delta.x <- 0.698000
delta.y <- 1.208971 
n.rows <- (49.567830)/delta.y
n.cols <- (11.168000)/delta.x









