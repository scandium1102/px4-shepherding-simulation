# PX4 Shepherding Simulation

A simulation-first integration prototype that connects a Python finite-state controller to PX4 SITL and Gazebo Classic through MAVROS. The project explores a shepherding-style multi-agent scenario; it is not a flight-tested autonomous system.

![PX4 simulation overview](assets/px4-overview.png)

## Stack

- PX4 SITL `v1.14.0-rc1`
- Gazebo Classic 11
- ROS Noetic and MAVROS
- Python 3.8 controller

## Control structure

The controller uses a five-state finite-state machine to coordinate high-level behavior:

1. initialize and connect;
2. arm and take off;
3. approach the simulated target area;
4. execute the shepherding behavior;
5. return or terminate safely in simulation.

## Evidence and limitations

The included figure documents the intended simulation integration. The work demonstrates SITL, ROS, MAVROS, and Python-controller integration. It does **not** claim real-world flight performance, vision-detector completion, collision safety, or field validation. See [docs/evidence.md](docs/evidence.md).

## Repository layout

```text
assets/       Public simulation overview
docs/         Evidence scope and reproducibility boundary
```

## Reuse

This is a portfolio case study, not a ready-to-fly vehicle package. Rebuild the simulation with your own PX4, Gazebo, ROS, and vehicle configuration before extending it.

## License

Apache-2.0. See [LICENSE](LICENSE).
