import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.time = 0

    def create_twist(self, linear_x, angular_z):
        msg = Twist()
        msg.linear.x = linear_x
        msg.angular.z = angular_z
        return msg

    def get_twist_msg(self):
        turn_speed = 1.568 # This turn speed allows approximately 90 degree angles when done for 5 seconds
        #Starts with a 45 degree turn
        if self.time < 2:
            msg = self.create_twist(0.0, turn_speed/2) #Divides speed by 2 to make a 90 degree turn into a 45 degree turn
        elif self.time >= 2 and self.time < 7:
            msg = self.create_twist(1.0, 0.0)
        elif self.time >= 7 and self.time < 9:
            msg = self.create_twist(0.0, turn_speed)
        elif self.time >= 12 and self.time < 17:
            msg = self.create_twist(1.0, 0.0)
        elif self.time >= 17 and self.time < 19:
            msg = self.create_twist(0.0, turn_speed)
        elif self.time >= 19 and self.time < 24:
            msg = self.create_twist(1.0, 0.0)
        elif self.time >= 24 and self.time < 26:
            msg = self.create_twist(0.0, turn_speed)
        elif self.time >= 26 and self.time < 31:
            msg = self.create_twist(1.0, 0.0)
        else:
            msg = self.create_twist(0.0, 0.0)
        return msg
    
    def timer_callback(self):
        msg = self.get_twist_msg()       
        self.publisher.publish(msg)
        self.time += 1
        print("time: {}".format(self.time))

def main(args=None):
    rclpy.init(args=args)

    turtle_controller = TurtleController()

    rclpy.spin(turtle_controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    turtle_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
