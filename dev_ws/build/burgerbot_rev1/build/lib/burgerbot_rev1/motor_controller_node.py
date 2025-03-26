#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import serial

class MotorControllerNode(Node):
    def __init__(self):
        super().__init__('motor_controller_node')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.cmd_vel_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Set up the serial connection to the ESP32 over USB.
        try:
            self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
            self.get_logger().info('Serial port /dev/ttyUSB0 opened successfully.')
        except Exception as e:
            self.get_logger().error('Failed to open serial port: {}'.format(e))
            self.ser = None

        # Set thresholds to decide if the command is significant.
        self.linear_threshold = 0.1   # m/s (adjust as needed)
        self.angular_threshold = 0.1  # rad/s (adjust as needed)

    def cmd_vel_callback(self, msg: Twist):
        # Read linear and angular values from the incoming Twist message.
        linear_x = msg.linear.x
        angular_z = msg.angular.z

        # Determine a discrete command.
        # Priority: If there is significant forward/backward motion, use that.
        # Otherwise, if there is a turn command, use that.
        if abs(linear_x) > self.linear_threshold:
            if linear_x > 0:
                command = "F"  # Forward
            else:
                command = "B"  # Backward
        elif abs(angular_z) > self.angular_threshold:
            if angular_z > 0:
                command = "L"  # Turn left
            else:
                command = "R"  # Turn right
        else:
            command = "S"      # Stop

        self.get_logger().info(f'Received cmd_vel: linear_x={linear_x:.2f}, angular_z={angular_z:.2f} => Command: {command}')

        # Send the command over serial.
        if self.ser is not None and self.ser.is_open:
            try:
                # We append a newline as a delimiter.
                self.ser.write((command + "\n").encode('utf-8'))
            except Exception as e:
                self.get_logger().error(f'Serial write error: {e}')
        else:
            self.get_logger().warn('Serial connection not available.')

def main(args=None):
    rclpy.init(args=args)
    node = MotorControllerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    # Clean up and close the serial port if needed.
    if node.ser is not None:
        node.ser.close()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
