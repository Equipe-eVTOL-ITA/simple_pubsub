import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile, HistoryPolicy, ReliabilityPolicy, DurabilityPolicy


class VelocityPublisher(Node):
    def __init__(self):
        super().__init__('velocity_publisher')

        # QoS configuration
        qos_profile = QoSProfile(
            depth=10,
            history=HistoryPolicy.KEEP_LAST,
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.VOLATILE
        )

        self.publisher = self.create_publisher(Twist, 'cmd_vel', qos_profile)

        # Parameter for linear velocity
        self.declare_parameter('linear_x', 0.5)
        self.linear_x = self.get_parameter('linear_x').get_parameter_value().double_value

        self.timer = self.create_timer(0.5, self.publish_velocity)

    def publish_velocity(self):
        msg = Twist()
        msg.linear.x = self.linear_x
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing linear x: {msg.linear.x}')


def main(args=None):
    rclpy.init(args=args)
    node = VelocityPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
