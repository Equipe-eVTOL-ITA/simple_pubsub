import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class SubscriberNode(Node):

    def __init__(self):
        super().__init__('subscriber_node')
        # Crie o subscriber aqui

    def odom_callback(self, msg):
        # Extraia e imprima x e y
        pass

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
