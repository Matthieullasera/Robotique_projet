import sys
import motor
import math
from constants import *


class Model(object):
    """
    Represents the robot's state 
    """

    def __init__(self):
        # Distance between the wheels
        self.l = L
        # Wheel radius
        self.r = R

        self.x = 0
        self.y = 0
        self.theta = 0

        self.x_goal = 0
        self.y_goal = 0
        self.theta_goal = 0

        self.m1 = motor.Motor()
        self.m2 = motor.Motor()

        self.acc = 0
        self.speed_acc = 0
        self.mode = 1

    def __repr__(self):
        s = "current : {} {} {}".format(self.x, self.y, self.theta)
        s = s + "\ngoal    : {} {} {}".format(self.x_goal, self.y_goal, self.theta_goal)
        s = s + "\nmotors    : {} {}".format(self.m1, self.m2)
        s = s + "acc={}, speed_acc={}, mode={}".format(
            self.acc, self.speed_acc, self.mode
        )
        return s

    def ik(self, linear_speed, rotational_speed):
        """Given the linear speed and the rotational speed, 
        returns the speed of the wheels in a differential wheeled robot
        
        Arguments:
            linear_speed {float} -- Linear speed (m/s)
            rotational_speed {float} -- Rotational speed (rad/s)
        
        Returns:
            float -- Speed of motor1 (m/s), speech of motor2 (m/s)
        """
        # TODO
        m1_speed = linear_speed + (L / 2) * rotational_speed   # dp = linear_speed , dtheta = rotational_spped
        m2_speed = linear_speed - (L / 2) * rotational_speed

        return m1_speed, m2_speed

    def dk(self, m1_speed=None, m2_speed=None):
        """Given the speed of each of the 2 motors (m/s), 
        returns the linear speed (m/s) and rotational speed (rad/s) of a differential wheeled robot
        
        Keyword Arguments:
            m1_speed {float} -- Speed of motor1 (m/s) (default: {None})
            m2_speed {float} -- Speed of motor2 (default: {None})
        
        Returns:
            float -- linear speed (m/s), rotational speed (rad/s)
        """
        # TODO
        linear_speed = (m1_speed + m2_speed) / 2
        rotation_speed = (m1_speed - m2_speed) / L
        return linear_speed, rotation_speed

    def update(self, dt):
        """Given the current state of the robot (speeds of the wheels) and a time step (dt), 
        calculates the new position of the robot.
        The speed of the wheels are assumed constant during dt.
        
        Arguments:
            dt {float} -- Travel time in seconds
        """
        # Going from wheel speeds to robot speed
        linear_speed, rotation_speed = self.dk(self.m1.speed, self.m2.speed)

        # TODO
        dx = (linear_speed / rotation_speed) * math.sin(rotation_speed)
        dy = (linear_speed / rotation_speed) * (1 - math.cos(rotation_speed))
        x_m = dx * math.cos(self.theta)- dy * math.sin(self.theta)
        y_m = dx * math.sin(self.theta) + dy * math.cos(self.theta)

        # Updating the robot position
        self.x = self.x + x_m  # TODO
        self.y = self.y + y_m  # TODO
        self.theta = self.theta + self.theta_goal  # TODO
