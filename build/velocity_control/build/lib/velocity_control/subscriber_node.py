import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile, HistoryPolicy, ReliabilityPolicy, DurabilityPolicy


class VelocitySubscriber(Node):
    def __init__(self):
        super().__init__('velocity_subscriber')

        qos_profile = QoSProfile(
            depth=10,
            history=HistoryPolicy.KEEP_LAST,
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.VOLATILE
        )

        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            qos_profile
        )

    def listener_callback(self, msg: Twist):
        self.get_logger().info(f'Received velocity: linear.x = {msg.linear.x}')


def main(args=None):
    rclpy.init(args=args)
    node = VelocitySubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
