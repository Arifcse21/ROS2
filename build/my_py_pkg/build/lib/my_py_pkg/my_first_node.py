#!/usr/bin/python3
import rclpy
from rclpy.node import Node


def main(args=None):
    rclpy.init(args=args)
    node = Node("py_test")  # don't use 'node' as tail. it would be redundant
    node.get_logger().info("Running ROS2 Node!...")
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
