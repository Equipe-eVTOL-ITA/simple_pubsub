import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalSubscriber(Node):
    def __init__(self):
        pass
        # Inicilizar o nó
        
        # Criar subscriber
        
        # Chamar a função de callback quando uma mensagem for recebida


    def listener_callback(self, msg):
        pass
        # Logar no console que a mensagem foi recebida


def main(args=None):
    rclpy.init(args=args)
    node = MinimalSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
