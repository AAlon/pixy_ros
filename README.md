# pixy_ros


## Clone & install dependencies

1. `mkdir -p ~/pixy_ws/src && cd ~/pixy_ws/src && git clone https://github.com/AAlon/pixy_ros && cd ..`
2. `rosdep install --from-paths src --ignore-src -r -y`

## Build

* `catkin_make`

## Run

* `source devel/setup.bash && rosrun pixy_node pixy_node`

`
