import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import random

class MentorPiController(Node):
    def __init__(self):
        # se inicializa el nodo con el nombre que le queramos dar
        super().__init__("actividad2_node")
        # se crea el publicador de velocidades
        self.cmd_vel_publisher_ = self.create_publisher(Twist, "/cmd_vel", 10)
        # se crea un timer para publicar la velocidad cada t segundos
        t = 0.5
        self.create_timer(t, self.publish_velocity)
        # se avisa que se inició el nodo
        self.get_logger().info("Nodo de comandos de velocidad iniciado.")
    
    def publish_velocity(self):
        msg = Twist()
        # ASEGURARSE DE LIMITAR LAS MAGNITUDES DE VELOCIDADES A 0.5
        msg.linear.x = random.uniform(-0.5, 0.5)
        msg.linear.y = random.uniform(-0.5, 0.5)
        msg.angular.z = random.uniform(-0.5, 0.5)
        self.cmd_vel_publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MentorPiController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass