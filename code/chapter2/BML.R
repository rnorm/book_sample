library(R6)

BML = R6Class(
  "BML",
  public = list(
    # alpha is the parameter of the uniform distribution to control particle distribution's density
    # m*n is the dimension of the lattice
    alpha = NULL,
    m = NULL,
    n = NULL,
    lattice = NULL,
    initialize = function(alpha, m, n) {
      self$alpha = alpha
      self$m = m
      self$n = n
      self$initialize_lattice()
    },
    initialize_lattice = function() {
      # 0 -> empty site
      # 1 -> blue particle
      # 2 -> red particle
      u = runif(self$m * self$n)
      # the usage of L is to make sure the elements in particles are of type integer;
      # otherwise they would be created as double
      particles = rep(0L, self$m * self$n)
      # https://en.wikipedia.org/wiki/Inverse_transform_sampling
      particles[(u > self$alpha) & (u <= (self$alpha + 1.0) / 2)] = 1L
      particles[u > (self$alpha + 1.0) / 2] = 2L
      self$lattice = array(particles, c(self$m, self$n))
    },
    odd_step = function() {
      blue.index = which(self$lattice == 1L, arr.ind = TRUE)
      # make a copy of the index
      blue.up.index = blue.index
      # blue particles move 1 site up
      blue.up.index[, 1] = blue.index[, 1] - 1L
      # periodic boundary condition
      blue.up.index[blue.up.index[, 1] == 0L, 1] = self$m
      # find which moves are feasible
      blue.movable = self$lattice[blue.up.index] == 0L
      # move blue particles one site up
      # drop=FALSE prevents the 2D array degenerates to 1D array
      self$lattice[blue.up.index[blue.movable, , drop = FALSE]] = 1L
      self$lattice[blue.index[blue.movable, , drop = FALSE]] = 0L
    },
    even_step = function() {
      red.index = which(self$lattice == 2L, arr.ind = TRUE)
      # make a copy of the index
      red.right.index = red.index
      # red particles move 1 site right
      red.right.index[, 2] = red.index[, 2] + 1L
      # periodic boundary condition
      red.right.index[red.right.index[, 2] == (self$n + 1L), 2] = 1
      # find which moves are feasible
      red.movable = self$lattice[red.right.index] == 0L
      # move red particles one site right
      self$lattice[red.right.index[red.movable, , drop = FALSE]] = 2L
      self$lattice[red.index[red.movable, , drop = FALSE]] = 0L
    }
  )
)

