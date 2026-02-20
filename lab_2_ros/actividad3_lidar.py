import math
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from rclpy.qos import qos_profile_sensor_data


class MentorPiSensor(Node):
    def __init__(self):
        super().__init__("actividad3_lidar_node")

        # OJO: en ROS2 el tópico del LiDAR es /scan (si el bridge está bien)
        self.sensor_subscriber = self.create_subscription(
        LaserScan,
        "/scan_raw",
        self.callback_sensor,
        qos_profile_sensor_data
    )

        self.get_logger().info("Nodo de captura de distancias iniciado.")

    def angle_to_index(self, theta_objetivo: float, msg: LaserScan) -> int:
        # diferencia angular respecto al inicio del scan
        diff = theta_objetivo - msg.angle_min

        # módulo 2pi para manejar wrap-around
        diff = diff % (2.0 * math.pi)

        # índice
        idx = int(diff / msg.angle_increment)

        # asegurar rango válido
        idx = max(0, min(idx, len(msg.ranges) - 1))
        return idx

    def valid_range(self, r: float, msg: LaserScan) -> bool:
        return math.isfinite(r) and (msg.range_min <= r <= msg.range_max)

    def callback_sensor(self, msg: LaserScan):
        # ángulos objetivo
        objetivos = {
            "Frente (0 rad)": 0.0,
            "Izquierda (+pi/2)": math.pi / 2.0,
            "Atras (pi)": math.pi,
            "Derecha (-pi/2)": -math.pi / 2.0,
        }

        salida = []
        for nombre, theta in objetivos.items():
            i = self.angle_to_index(theta, msg)
            d = msg.ranges[i]
            if self.valid_range(d, msg):
                salida.append(f"{nombre}: {d:.2f} m")
            else:
                salida.append(f"{nombre}: inf")

        self.get_logger().info(" | ".join(salida))


def main(args=None):
    rclpy.init(args=args)
    node = MentorPiSensor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()