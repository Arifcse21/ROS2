#!/usr/bin/python
import rclpy
from rclpy.node import Node


class MyNode(Node):
    def __init__(self):
        super(MyNode, self).__init__("first_node")
        self.get_logger().info("Hello world ROS2")


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()

    rclpy.spin(node)


    


    rclpy.shutdown()


if __name__ == '__main__':
    main()