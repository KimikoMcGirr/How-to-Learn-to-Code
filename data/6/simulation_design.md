# Viral Simulation

This document outlines the classes that need to be implemented for the simulation. It also explicitly lays out all the necessary details covering the behavior of each class and what functionality of the simulation should be handled by each type of class.

Classes
-------

* Food
* Viruses
* Macrophages
* Simulation

Food
----

* Each particle is located at random anywhere in the simulated tissue environment.
* It's position can be described by an x,y coordinate system where x and y are integers in the range 0 to 19, inclusive.
* It also has a starting mass of 10.
* Each time step, the mass has a 50% chance of degrading by 1.
* If the mass of a particle reaches 0, the particle disappears.

Virus
-----

* Like food, viruses have a position and mass of 10.
* Additionally, they also have a defense attribute.
  * The defense attribute can always be calculated as the square root virus mass divided by 20.
* Viruses are capable of moving around the tissue.
  * They can move a single step in any direction each time step.
  * That is, both x and y can independently increase by -1, 0, or 1.
  * The virus must stay in the bounds of the simulation while moving.
  * That means, a virus can potentially spend a turn by attempting to move but not changing position.
  * To phase it another way, if a virus does not start along an edge or in a corner, then it can end in any of nine positions.
* Any time a virus is in the same location as a food particle, it consumes the food.
  * Food consumption increase the mass of the virus by the mass of the food consumed.
* If a virus reaches a mass of 25, it divides.
  * Division resets the mass of the virus to 10.
  * It also creates a second virus, with a position that is the same as the original virus and a mass of 10.

Macrophage
----------

* Macrophages also have positions, but there is no need to keep track of their mass.
* Each time step, a macrophage can move in one of two ways.
  * It can move five steps in a straight line (up, down, left, or right), or it can take three steps at random.
  * If it moves at random, -1, 0, or 1 is added to x or y (not both) each step.
  * The macrophage must stay in the bounds of the simulation while moving.
  * The macrophage has an equal probability of moving in a straight line or at random.
  *  If the macrophage moves in a straight line (up, down, left, right), it moves five steps per time step.
* If it runs into a virus, it has a baseline 35% chance of destroying the virus.
* The macrophage will continue to move even after running into a virus.
* If it moves at random (up, down, left, right), it takes three steps,
but it has a baseline 50% chance of killing any viruses.
* This baseline probability can be supplemented by a 'history' probability.
  * For each virus a give macrophage kills, this 'history' attribute is increased by 5%.
  * This increased probability of killing a virus can be as large as 50%
  * Finally, any probability a macrophage has of destroying a virus is reduced by the defense attribute of the attacked virus.
  * If the virus' defense is equal to or larger than the macrophage's history-supplemented probability of success, then the virus will not be destroyed.

Simulation
----------

* The Simulation is responsible for a single run of an experiment/trial.
* It's attributes should contain individual collections of food, viruses, and macrophages.
* It must keep track of the time steps, and update all data each time step.
* The simulation should also create 40 new particles of food each time step.

The update order should be:

* Viruses move
  * and eat
  * and divide
* Macrophages move
  * and kill
* Food degrades
  * and spawns


Notes
-----

* Each time step in the simulation is one hour.
* The simulation should not last longer than 100 hours (i.e. time steps).
