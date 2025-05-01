import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class PublisherNode(Node):

    def __init__(self):
        super().__init__('publisher_node')
        # Crie o publisher aqui
        # Crie o timer aqui

    def publish_velocity(self):
        # Crie a mensagem Twist aqui e publique
        pass

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
