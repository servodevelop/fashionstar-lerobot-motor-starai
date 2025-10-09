# LeRobot + xArm Integration

Brings a simple integration with [LeRobot](https://github.com/huggingface/lerobot) and [xArm](https://github.com/xArm-Developer).

## Getting Started

```bash
pip install lerobot-motor-starai

lerobot-teleoperate \
    --robot.type=lerobot_robot_xarm \
    --robot.id=black \
    --teleop.type=keyboard_ee \
    --fps=60
```

## Development

Install the package in editable mode:
```bash
git clone https://github.com/SpesRobotics/lerobot-robot-xarm.git
cd lerobot_motor_starai
pip install -e .
```
