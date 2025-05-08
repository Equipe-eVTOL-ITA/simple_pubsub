# Importar ros2 class for python

# Importar a classe Node do rclpy

from std_msgs.msg import String

class MinimalPublisher(Node):
    def __init__(self):
        pass
        # Inicilizar o no

        # Criar publisher

        # Criar timer com a função de callback


    def timer_callback(self):
        pass
        # Inicilizar mensagem

        # Popular data da mensagem

        # Publicar a mensagem

        # Logar no console que a mensagem foi publicada


def main(args=None):
    rclpy.init(args=args)
    # Criar o nó (objeto) da classe MinimalPublisher
    node = MinimalPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
